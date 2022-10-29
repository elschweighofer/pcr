# type: ignore
from datetime import datetime
from pydantic import BaseModel, ValidationError, validator
from app.utils.database import database 

class Sample(BaseModel):
    barcode: str
    positive: bool
    @validator('barcode')
    def barcode_cannot_contain_yz(cls, v):
        if 'x' or 'y' in v:
            raise ValueError('cannot contain ambigiuos chars: x, y')
        return v.title()

collection = database.sample

async def fetch_one_sample(barcode):
    document = await collection.find_one({"barcode": barcode})
    return document

async def fetch_all_samples():
    samples = []
    cursor = collection.find({})
    async for document in cursor:
        samples.append(Sample(**document))
    return samples

async def create_sample(sample):
    document = sample
    result = await collection.insert_one(document)
    return document

async def update_sample(barcode, positive):
    await collection.update_one({"barcode": barcode},{'$set': {"positive": positive}})
    document = await collection.find_one({"barcode": barcode})
    return document

async def remove_sample(barcode):
   await collection.delete_one({"barcode": barcode})
   return True