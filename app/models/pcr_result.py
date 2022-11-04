from datetime import datetime
from pydantic import BaseModel, validator
from app.utils.database import database
from app.models.sample import Sample, create_sample
from app.models.pcr_kit import PcrKit
from bson.son import SON


collection = database.result


class PcrResult (BaseModel):
    ts: datetime = None #type: ignore
    result_values: dict
    analyzer: str
    @validator('ts', pre=True, always=True)
    def set_ts_now(cls, v):
        return v or datetime.now()

    @validator('analyzer')
    def check_analyzer(cls,v):
        pass


async def create_result(pcr_result):
    document = pcr_result
    results_main = await collection.insert_one(document)
    results_embedded = await create_sample(pcr_result.get("sample"))
    return document

#cursor = db.inventory.find({"size": SON([("h", 14), ("w", 21), ("uom", "cm")])})
async def fetch_by_sample(barcode):
    results = []
    cursor =  collection.find({"sample": SON([("barcode", barcode)])})
    async for document in cursor:
        results.append(PcrResult(**document))
    return results


async def fetch_all_results():
    results = []
    cursor = collection.find({})
    async for document in cursor:
        results.append(PcrResult(**document))
    return results


async def update_result(barcode, positive):
    pass


async def remove_result(barcode):
    result = await collection.delete_one({"barcode": barcode})
    return result
