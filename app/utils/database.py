import motor.motor_asyncio
from dotenv import load_dotenv
import os    
#uri = "mongodb://user:pass@localhost:27017/database_name"

load_dotenv()
MONGO_DB_HOST = os.getenv("MONGO_DB_HOST")
MONGO_DB_PORT = os.getenv("MONGO_DB_PORT") # Default 27017
MONGO_DB_USER = os.getenv("MONGO_DB_USER")
MONGO_DB_PASSWORD = os.getenv("MONGO_DB_PASSWORD")

if not MONGO_DB_PORT:
    MONGO_DB_PORT = 27017

if MONGO_DB_USER:
    MONGO_DB_URI = f"mongodb://{MONGO_DB_USER}:{MONGO_DB_PASSWORD}@{MONGO_DB_HOST}:{MONGO_DB_PORT}/"
else:
    MONGO_DB_URI = f"mongodb://{MONGO_DB_HOST}:{MONGO_DB_PORT}/"



client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI)
database = client.PCR




