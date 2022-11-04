from app.models.pcr_result import create_result


seed_data = [{
  "sample": {
    "barcode": "Seed10000",
    "ts": "2022-11-04T15:53:31.534Z"
  },
  "ts": "2022-11-04T15:53:31.534Z",
  "kit": {
    "name": "string",
    "values": [
      "string"
    ]
  },
  "ct_values": {}
},
{
  "sample": {
    "barcode": "Seed10001",
    "ts": "2022-11-04T15:53:31.534Z"
  },
  "ts": "2022-11-04T15:53:31.534Z",
  "kit": {
    "name": "string",
    "values": [
      "string"
    ]
  },
  "ct_values": {}
},
{
  "sample": {
    "barcode": "Seed10002",
    "ts": "2022-11-04T15:53:31.534Z"
  },
  "ts": "2022-11-04T15:53:31.534Z",
  "kit": {
    "name": "string",
    "values": [
      "string"
    ]
  },
  "ct_values": {}
}
]
async def populate():
    for result in seed_data:
        await create_result(result)