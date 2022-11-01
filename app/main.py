from app.models.sample \
    import create_sample, fetch_all_samples, fetch_one_sample, remove_sample, update_sample, Sample
from app.models.pcr_result\
    import create_result, fetch_all_results, fetch_by_sample, remove_result, update_result, PcrResult
from app.models.pcr_kit \
    import fetch_all_kits, create_kit, PcrKit
from fastapi import FastAPI, HTTPException
from app.utils.cache import timed_lru_cache, cache_response

# App Object
app = FastAPI(docs_url="/", redoc_url=None)


@app.post("/api/v1/samples/", response_model=Sample)
async def post_sample(sample: Sample):
    response = await create_sample(sample.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@app.get("/api/v1/samples/")
@timed_lru_cache(seconds=5, maxsize=1000)
async def get_sample():
    response = await fetch_all_samples()
    return response


@app.get("/api/v1/samples/{barcode}", response_model=Sample)
@timed_lru_cache(seconds=30, maxsize=200)
async def get_sample_by_barcode(barcode: str, q: str | None = None):
    response = await fetch_one_sample(barcode)
    if response:
        return response
    raise HTTPException(404, f"There is no Sample with the barcode {barcode}")


@app.put("/api/v1/samples{barcode}", response_model=Sample)
async def put_sample(barcode: str, positive: bool):
    response = await update_sample(barcode, positive)
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@app.delete("/api/v1/samples/{barcode}")
async def delete_sample(barcode):
    response = await remove_sample(barcode)
    if response:
        return "Successfully deleted sample"
    raise HTTPException(404, f"There is no Sample with the barcode {barcode}")


@app.post("/api/v1/results/", response_model=PcrResult)
async def post_result(result: PcrResult):
    response = await create_result(result.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@app.get("/api/v1/results/")
async def get_all_results():
    response = await fetch_all_results()
    return response


@app.get("/api/v1/kits/")
@cache_response
async def get_all_kits():
    response = await fetch_all_kits()
    return response


@app.post("/api/v1/kits/", response_model=PcrKit)
async def post_kit(kit: PcrKit):
    response = await create_kit(kit.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")
