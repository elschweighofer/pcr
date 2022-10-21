from datetime import datetime
from pydantic import BaseModel

class Sample(BaseModel):
    barcode: str
    positive: bool

class Analyzer(BaseModel):
    name: str
    outputs: list[str]

class Device(BaseModel):
    name: str
    kind: Analyzer

class Result (BaseModel):
    sample: Sample
    ct: str
    control: str
    timestamp: datetime

class Batch (BaseModel):
    results: list[Result]
    device: Device
