from app.database import (
    fetch_one_sample,  # type: ignore
    fetch_all_samples,  # type: ignore
    create_sample,  # type: ignore
    update_sample,  # type: ignore
    remove_sample  # type: ignore
)
from app.model import *
from fastapi import FastAPI, HTTPException

# App Object
app = FastAPI()


@app.post("/api/v1/sample/", response_model=Sample)
async def post_sample(sample: Sample):
    response = await create_sample(sample.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@app.get("/api/v1/sample/")
async def get_sample():
    response = await fetch_all_samples()
    return response


@app.get("/api/v1/samples/{barcode}", response_model=Sample)
async def get_sample_by_barcode(barcode: str, q: str | None = None):
    response = await fetch_one_sample(barcode)
    if response:
        return response
    raise HTTPException(404, f"There is no Sample with the barcode {barcode}")


@app.put("/api/v1/samples{barocde}", response_model=Sample)
async def put_sample(barcode: str, positive: bool):
    response = await update_sample(barcode, positive)
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@app.delete("/api/v1/sample/{barcode}", response_model=Sample)
async def remove_sample(barcode: str):
    response = await remove_sample(barcode)
    if response:
        return response
    raise HTTPException(404, f"There is no Sample with the barcode {barcode}")
