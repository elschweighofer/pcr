# type: ignore
import motor.motor_asyncio
from dotenv import load_dotenv
import os    

load_dotenv()
MONGO_DB = os.getenv("MONGO_DB")


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)
database = client.PCR



