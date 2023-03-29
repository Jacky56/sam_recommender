import pandas as pd
import jellyfish
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


class fake_model():
    def __init__(self):
        self.md = pd.read_csv("./dataset/curated.csv")
        self.md["title_metaphone"] = self.md["title_metaphone"].fillna("")
        self.titles = self.md["title"]
        self.indices = pd.Series(self.md.index, index=self.md["title"])
        self.md["description"] = self.md["overview"]+ self.md["genres"] + self.md["keywords"]
        self.md["description"] = self.md["description"].fillna("") 
        tf = TfidfVectorizer(analyzer="word",ngram_range=(1, 2),min_df=0, stop_words="english")
        tfidf_matrix = tf.fit_transform(self.md["description"])
        self.cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)


    def _correct_bad_english(self, title: str) -> str:
        if title in self.indices:
            return title
        title_metaphone = jellyfish.metaphone(title)
        return self.titles[self.md["title_metaphone"].apply(lambda x: jellyfish.jaro_similarity(title_metaphone, x)).idxmax()]


    def get_recommendations(self, title_input: str) -> dict:
        title_corrted = self._correct_bad_english(title_input)
        idx = self.indices[title_corrted]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movie_indices = [i[0] for i in sim_scores]
        d = {
            "title_input": title_input,
            "title_corrted": title_corrted,
            "body": self.md.iloc[movie_indices][["title",
                                                 "imbd_link",
                                                 "genres",
                                                 "overview"
                                                 ]].to_dict("index")
        }
        return d
