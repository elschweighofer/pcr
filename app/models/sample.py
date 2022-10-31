from datetime import datetime
from pydantic import BaseModel, ValidationError, validator
from app.utils.database import database 

class Sample(BaseModel):
    barcode: str
    ts: datetime = None #type: ignore
    
    @validator('barcode')
    def barcode_cannot_contain_yz(cls, v):
        if 'y' in v or 'z' in v:
            raise ValueError('cannot contain ambigiuos chars: y,z')
        return v.title()
        
    @validator('ts', pre=True, always=True)
    def set_ts_now(cls, v):
        return v or datetime.now()

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