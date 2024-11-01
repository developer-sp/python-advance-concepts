import asyncio

async def divide_numbers(x, y):
    try:
        print(f"Dividing {x} by {y}")
        result = x / y
        await asyncio.sleep(1)  # Simulating an async operation
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero!")

async def main():
    await asyncio.gather(
        divide_numbers(10, 2),
        divide_numbers(5, 0)
    )

asyncio.run(main())