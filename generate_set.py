import pandas as pd
import re
import jellyfish


if __name__ == "__main__":
    keywords = pd.read_csv("./dataset/keywords.csv")
    keywords["id"] = keywords["id"].astype("int")

    md = pd. read_csv("./dataset/movies_metadata.csv")
    md["id"] = md["id"].astype("int")
    md = md.merge(keywords, on="id")
    md["genres"] = md["genres"].fillna("").apply(eval).apply(lambda x: " ".join([i["name"] for i in x]) if isinstance(x, list) else [])
    md["keywords"] = md["keywords"].fillna("").apply(eval).apply(lambda x: " ".join([i["name"] for i in x]) if isinstance(x, list) else [])
    md["description"] = md["overview"]+ md["genres"] + md["keywords"]
    md["title_metaphone"] = md["title"].fillna("").apply(jellyfish.metaphone)
    md["description"] = md["description"].fillna("").apply(lambda x: x.lower()).apply(lambda x: re.sub("\W+"," ", x))
    md["imbd_link"] = md["imdb_id"].apply(lambda x: f"https://www.imdb.com/title/{x}/" if x else None)

    md = md[["title","title_metaphone", "imbd_link", "genres", "keywords", "overview", "description"]]
    md[:9000].to_csv("./dataset/curated.csv",index=False)
