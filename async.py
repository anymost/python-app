import asyncio


async def good():
    print("start")
    await asyncio.sleep(100)
    print("end")


async def concurrent():
    task1 = asyncio.create_task(good())
    task2 = asyncio.create_task(good())
    await task1
    await task2


async def compute(start, end: int) -> int:
    result = 0
    for i in range(start, end):
        result += i
    return result


async def concurrent_sum():
    task1 = asyncio.create_task(compute(0, 100000000))
    task2 = asyncio.create_task(compute(100000000, 200000000))
    task3 = asyncio.create_task(compute(200000000, 300000000))
    task4 = asyncio.create_task(compute(300000000, 400000000))
    task5 = asyncio.create_task(compute(400000000, 500000000))
    task6 = asyncio.create_task(compute(500000000, 600000000))
    result1 = await task1
    result2 = await task2
    result3 = await task3
    result4 = await task4
    result5 = await task5
    result6 = await task6
    print(result1 + result2 + result3 + result4 + result5 + result6)


asyncio.run(concurrent_sum())
