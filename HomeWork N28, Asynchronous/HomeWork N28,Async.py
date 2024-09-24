import asyncio
import time
import random


# task N1
async def task1():
    await asyncio.sleep(2)
    print('Task 1 Done')


async def task2():
    await asyncio.sleep(5)
    print('Task 2 Done')


async def main():
    start_time = time.time()

    await asyncio.create_task(task1())
    await asyncio.create_task(task2())

    end_time = time.time()

    result = (end_time - start_time)

    print("Elapsed time : {}".format(result))


if __name__ == '__main__':
    asyncio.run(main())


# task N2

async def task(name, delay):
    print("Task " + name + " started")
    await asyncio.sleep(delay)
    print("Task " + name + " finished")
    return name


async def main():
    start = time.time()

    task_list = []

    for i in range(1, 11):
        task_name = "Task " + str(i)
        delay = random.randint(1, 10)
        task_list.append(task(task_name, delay))

    await asyncio.gather(*task_list)

    end = time.time()
    result = end - start
    print("Execution time: " + str(result))


if __name__ == "__main__":
    asyncio.run(main())


# Task N3

async def square(number):
    return number ** 2


async def check_number_square(number):
    if number % 2 == 0:
        return await square(number)
    else:
        return "This number isn't even"


async def main():
    start = time.time()

    number = int(input("Enter a number: "))

    square_task = asyncio.create_task(square(number))
    check_number_task = asyncio.create_task(check_number_square(number))

    square_result, check_number_result = await asyncio.gather(square_task, check_number_task)

    end = time.time()

    time_taken = end - start

    print(f"Square of {number} is: {square_result}")
    print(f"Result is: {check_number_result}")
    print(f"Time taken: {time_taken}")


if __name__ == "__main__":
    asyncio.run(main())
