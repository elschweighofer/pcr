from app.models.result\
    import create_result, fetch_all_results, fetch_by_sample, remove_result, update_result, Result
from fastapi import FastAPI, HTTPException
from app.utils.logging import logger
from app.utils.database import database

# App Object
app = FastAPI(docs_url="/", redoc_url=None)

@app.on_event("startup")
async def startup_event():
    result = await database.result.create_index("sample_barcode", unique=True)
    return 'created index'


@app.post("/results/", tags=["results"], response_model=Result)
async def post_result(result: Result):
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

@app.delete("/delete/{barcode}",tags=["results"])
async def delete_result(barcode):
    response = await remove_result(barcode)
    return response
