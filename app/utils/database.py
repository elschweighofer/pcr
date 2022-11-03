# type: ignore
import motor.motor_asyncio
from dotenv import load_dotenv
import os    

MONGO_DB_URI = os.getenv("MONGO_DB_URI")


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI)
database = client.PCR



