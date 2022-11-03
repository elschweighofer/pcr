from datetime import datetime
import uuid
from pydantic import BaseModel, Field, ValidationError, validator
from app.utils.database import database




class Sample(BaseModel):
    #id: str = Field(default_factory=uuid.uuid4, alias="_id")
    barcode: str #= Field(...)
    ts: datetime = None  # type: ignore

    @validator('barcode')
    def barcode_cannot_contain_yz(cls, v):
        if 'y' in v or 'z' in v:
            raise ValueError('cannot contain ambigiuos chars: y,z')
        return v.title()

    @validator('ts', pre=True, always=True)
    def set_ts_now(cls, v):
        return v or datetime.now()
    class Config:
        allow_population_by_field_name = True


collection = database.sample


async def create_sample(sample):
    document = sample
    results = await collection.insert_one(document)
    return document


async def fetch_one_sample(barcode):
    document = await collection.find_one({"barcode": barcode})
    return document


async def fetch_all_samples():
    samples = []
    cursor = collection.find({})
    async for document in cursor:
        samples.append(Sample(**document))
    return samples


async def remove_sample(barcode):
    sample =  await collection.find_one({"barcode": barcode}) 
    if sample is not None:
        await collection.delete_one({"barcode": barcode})
        return True
    return False
