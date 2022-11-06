from app.models.result import create_result
seed_data= []
async def populate():
    for result in seed_data:
        await create_result(result)