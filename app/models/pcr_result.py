from datetime import datetime
from pydantic import BaseModel, validator
from app.utils.database import database
from app.models.sample import Sample
from app.models.pcr_kit import PcrKit
collection = database.result


class PcrResult (BaseModel):
    sample: Sample
    ts: datetime = None #type: ignore
    kit : PcrKit
    ct_values: dict

    @validator('ts', pre=True, always=True)
    def set_ts_now(cls, v):
        return v or datetime.now()

    #validator('ct'


async def create_result(result):
    document = result
    result = await collection.insert_one(document)
    return document


async def fetch_by_sample(sample):
    document = await collection.find_one({"barcode": sample.barcode})
    return document


async def fetch_all_results():
    results = []
    cursor = collection.find({})
    async for document in cursor:
        results.append(PcrResult(**document))
    return results


async def update_result(barcode, positive):
    await collection.update_one({"barcode": barcode}, {'$set': {"positive": positive}})
    document = await collection.find_one({"barcode": barcode})
    return document


async def remove_result(barcode):
    result = await collection.delete_one({"barcode": barcode})
    return result
