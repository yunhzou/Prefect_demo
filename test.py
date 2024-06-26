import asyncio

async def my_async_function():
    await asyncio.sleep(1)  # Simulate a delay
    return "Hello, World!"

async def main():
    result = await my_async_function()
    print(result)

# Run the main function
asyncio.run(main())
