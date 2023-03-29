import json
from fastapi import FastAPI
from commons import fake_model
from fastapi.responses import PlainTextResponse

app = FastAPI()
recommender = fake_model()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/search/{name}", response_class=PlainTextResponse)
def read_item(name: str) -> dict:
    d =recommender.get_recommendations(name)
    return json.dumps(d,indent=4)
