from fastapi import FastAPI


from queries import (
    get_averages,
    top_genes,
    filter_genes
)

app = FastAPI()


@app.get("/")
def root():
    return {"status": "Neo4j cell death genes API running"}


@app.get("/averages")
def averages():
    return get_averages()


@app.get("/top-genes")
def get_top():
    return top_genes()


@app.get("/filter")
def get_filtered(
    area_min: float,
    area_max: float,
    count_min: float,
    count_max: float
):
    return filter_genes(area_min, area_max, count_min, count_max)