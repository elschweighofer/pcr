from pydantic import BaseModel, validator
from app.utils.database import database


class PcrKit (BaseModel):
    name: str
    values: tuple
    #class Config:
    #   allow_mutation = False


collection = database.kit


async def fetch_all_kits():
    kits = []
    cursor = collection.find({})
    async for document in cursor:
        kits.append(PcrKit(**document))
    return kits


async def create_kit(kit):
    document = kit
    result = await collection.insert_one(document)
    return document
