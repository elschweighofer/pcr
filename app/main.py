from app.models.sample \
    import create_sample, fetch_all_samples, fetch_one_sample, remove_sample, Sample
from app.models.pcr_result\
    import create_result, fetch_all_results, fetch_by_sample, remove_result, update_result, PcrResult
from app.models.pcr_kit \
    import fetch_all_kits, create_kit, PcrKit
from fastapi import FastAPI, HTTPException
from app.utils.cache import timed_lru_cache, cache_response


# App Object
app = FastAPI(docs_url="/", redoc_url=None)


@app.post("/samples/", tags=["samples"], response_model=Sample)
async def post_sample(sample: Sample):
    response = await create_sample(sample.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@app.get("/samples/", tags=["samples"])
async def get_sample():
    response = await fetch_all_samples()
    return response


@app.get("/samples/{barcode}", tags=["samples"], response_model=Sample)
#@timed_lru_cache(seconds=30, maxsize=200)
async def get_sample_by_barcode(barcode: str, q: str | None = None):
    response = await fetch_one_sample(barcode)
    if response:
        return response
    raise HTTPException(404, f"There is no Sample with the barcode {barcode}")



@app.delete("/samples/{barcode}", tags=["samples"])
async def delete_sample(barcode):
    response = await remove_sample(barcode)
    if response:
        return "Successfully deleted sample"
    raise HTTPException(404, f"There is no Sample with the barcode {barcode}")


@app.post("/results/", tags=["results"], response_model=PcrResult)
async def post_result(result: PcrResult):
    response = await create_result(result.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@app.get("/results/", tags=["results"])
async def get_all_results():
    response = await fetch_all_results()
    return response

@app.get("/results/{barcode}",tags=["results"])
async def get_result_by_sample(barcode):
    response = await fetch_by_sample(barcode)
    return response

@app.get("/kits/", tags=["kits"])
#@cache_response
async def get_all_kits():
    response = await fetch_all_kits()
    return response


@app.post("/kits/",  tags=["kits"], response_model=PcrKit)
async def post_kit(kit: PcrKit):
    response = await create_kit(kit.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.delete("/delete/{barcode}",tags=["results"])
async def remove_result(barcode):
    response = await fetch_by_sample(barcode)
    return response