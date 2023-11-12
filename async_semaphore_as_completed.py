# Semaphore as_completed

import aiohttp
import asyncio
import time


async def fetch(sema, url, session):
    # Get the goods
    async with sema, session.get(url) as response:
        return await response.json()


async def main():
    start_time = time.time()

    # ##################################################
    # This prints results after they are done
    # Using a Semaphore to create a pool of threads

    print('Async Semaphore as_completed')

    url = 'https://swapi.dev/api/people/{}'

    tasks = []
    # Create an instance of Semaphore
    sema = asyncio.Semaphore(5)

    async with aiohttp.ClientSession() as session:
        for i in range(1, 10):
            # Pass the Semaphore and session to every GET request
            task = fetch(sema, url.format(i), session)
            tasks.append(task)

        # Do it
        for future in asyncio.as_completed(tasks):
            result = await future
            print(f'{result["name"]}')
            print(f'{result["birth_year"]}')
            print(f'{result["gender"]}')

    script_time = time.time() - start_time
    print(f'The script took {script_time} second !')


if __name__ == '__main__':
    asyncio.run(main())
