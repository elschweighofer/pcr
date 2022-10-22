# type: ignore
from datetime import datetime
from pydantic import BaseModel
from app.utils.database import database 

class result(BaseModel):
    barcode: str
    positive: bool

collection = database.result


class Result (BaseModel):
    result: result
    ct: str
    control: str
    timestamp: datetime




async def fetch_one_result(barcode):
    document = await collection.find_one({"barcode": barcode})
    return document

async def fetch_all_results():
    results = []
    cursor = collection.find({})
    async for document in cursor:
        results.append(result(**document))
    return results

async def create_result(result):
    document = result
    result = await collection.insert_one(document)
    return document

async def update_result(barcode, positive):
    await collection.update_one({"barcode": barcode},{'$set': {"positive": positive}})
    document = await collection.find_one({"barcode": barcode})
    return document

async def remove_result(barcode):
    result = await collection.delete_one({"barcode": barcode})
    return result

