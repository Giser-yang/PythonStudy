# import asyncio
#
#
# async def test():
#     print("hello")
#     await asyncio.sleep(1)
#     print("world")
#
# asyncio.run(test())

# import asyncio
# import time
#
#
# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
#
#
# async def main():
#     print(f"started at {time.strftime('%X')}")
# # 按顺序等待执行 3秒
#     await say_after(1, 'hello')
#     await say_after(2, 'world')
#
#     print(f"finished at {time.strftime('%X')}")
#
#
# asyncio.run(main())

# import asyncio
# import time
#
# #  并发 运行两个 say_after 协程  两秒
# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
#
#
# async def main():
#     task1 = asyncio.create_task(say_after(1, 'hello'))
#     task2 = asyncio.create_task(say_after(2, 'world'))
#     print(f"start at {time.strftime('%X')}")
#     await task1
#     await task2
#     print(f"finished at {time.strftime('%X')}")
#
# asyncio.run(main())

# import asyncio
# import datetime
#
#
# async def display_date():
#     loop = asyncio.get_running_loop()
#     end_time = loop.time() + 5
#     print(loop.time())
#     while True:
#         print(datetime.datetime.now())
#         if (loop.time() + 1) >= end_time:
#             break
#         await asyncio.sleep(1)
#
#
# asyncio.run(display_date())

import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    # Schedule three calls *concurrently*:
    #  如果所有可等待对象都成功完成，结果将是一个由所有返回值聚合而成的列表。结果值的顺序与 aws 中可等待对象的顺序一致。
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)


asyncio.run(main())
