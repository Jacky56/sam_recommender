# sam_recommender

ripped from here:

https://www.kaggle.com/code/rounakbanik/movie-recommender-systems/notebook


libraries used:
- [requirements.txt](./requirements.txt)

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
