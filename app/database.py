# type: ignore
import motor.motor_asyncio
from app.model import *
from dotenv import load_dotenv
import os    

load_dotenv()
MONGO_DB = os.getenv("MONGO_DB")


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)
database = client.PCR
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
    result = await collection.delete_one({"barcode": barcode})
    return result
