import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)
    print("World!")

# Running the async function
asyncio.run(say_hello())