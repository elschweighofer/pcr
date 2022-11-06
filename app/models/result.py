from datetime import datetime
from pydantic import BaseModel, validator, root_validator
from app.utils.database import database
from bson.son import SON
from pymongo.errors import DuplicateKeyError


collection = database.result


class Sample (BaseModel):
    barcode: str
    material: str


class Kit(BaseModel):
    id: int
    name: str
    kit_values: list[str]


class Result (BaseModel):
    sample: Sample
    kit_id: str
    analyser_id: str
    result_values: dict[str,float]

async def create_result(result):
    document = result
    try:
        statement = await collection.insert_one(document)
        return document
    except DuplicateKeyError:
        return False



async def fetch_by_sample(barcode):
    fetched = []
    cursor = collection.find({"sample": SON([("barcode", barcode)])})
    async for document in cursor:
        fetched.append(Result(**document))
    return fetched

async def fetch_all_results():
    fetched = []
    cursor = collection.find()
    async for document in cursor:
        fetched.append(Result(**document))
    return fetched


async def update_result(barcode):
    statement = collection.update_one()

    pass


async def remove_result(barcode):
    sample =  await collection.find_one({"barcode": barcode}) 
    if sample is not None:
        await collection.delete_one({"barcode": barcode})
        return True
    return False