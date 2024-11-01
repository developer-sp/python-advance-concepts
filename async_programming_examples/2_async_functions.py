import asyncio

async def task_1():
    print("Task 1 starting")
    await asyncio.sleep(2)
    print("Task 1 done")

async def task_2():
    print("Task 2 starting")
    await asyncio.sleep(1)
    print("Task 2 done")

async def main():
    await task_1()
    await task_2()

asyncio.run(main())
