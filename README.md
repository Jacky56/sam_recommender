# sam_recommender

ripped from here:

https://www.kaggle.com/code/rounakbanik/movie-recommender-systems/notebook


libraries used:
- [requirements.txt](./requirements.txt)

## How to use

- To read the docs: **https://movie-recommender-lkdpdhyb4q-od.a.run.app/docs**
- To search for a movie: **https://movie-recommender-lkdpdhyb4q-od.a.run.app/search/{name}**
- To test if it works: **https://movie-recommender-lkdpdhyb4q-od.a.run.app**

Exmaple:
- https://movie-recommender-lkdpdhyb4q-od.a.run.app/search/god+father
- https://movie-recommender-lkdpdhyb4q-od.a.run.app/search/ice+age

## how to build container

```bash
docker build -t <name of container> .
```

example:
```bash
docker build -t movie_recommend .
```

## how to run container

```bash
docker run -e PORT=8080 <name of container>
```

example:
```bash
docker run -e PORT=8080 movie_recommend
```
