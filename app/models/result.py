from datetime import datetime
from pydantic import BaseModel, validator, root_validator
from app.utils.database import database
from bson.son import SON
from pymongo.errors import DuplicateKeyError


collection = database.result


class Kit(BaseModel):
    id: int
    name: str
    kit_values: list[str]


class Result (BaseModel):
    sample_barcode: str
    kit_id: str
    analyser_id: str
    result_values: dict[str, float]


async def create_result(result):
    document = result
    try:
        statement = await collection.insert_one(document)
        return document
    except DuplicateKeyError:
        return False


async def fetch_by_sample(barcode):
    fetched = []
    cursor = collection.find({"sample_barcode": barcode})
    async for document in cursor:
        fetched.append(Result(**document))
    return fetched


async def fetch_all_results():
    fetched = []
    cursor = collection.find()
    async for document in cursor:
        fetched.append(Result(**document))
    return fetched


async def update_result(result):
    old_document = await collection.find_one({'sample_barcode': result.get('sample_barcode')})
    statement = collection.replace_one()
    _id = old_document.get('_id')
    result = await collection.replace_one({'_id': _id}, result)
    new_document = await collection.find_one({'_id': _id})
    return new_document


async def remove_result(sample_barcode):
    sample = await collection.find_one({"sample_barcode": sample_barcode})
    if sample is not None:
        await collection.delete_one({"sample_barcode": sample_barcode})
        return f'Deleted Result with sample_barcode {sample_barcode}'
    return f'No Result with sample_barcode {sample_barcode}'
