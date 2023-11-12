# semaphore gather

import aiohttp
import asyncio
import time


async def fetch(sema, url, session):
    async with sema, session.get(url) as response:
        return await response.json()


async def main():
    start_time = time.time()

    # ##################################################
    # This prints results after they are done
    # Using a Semaphore to create a pool of threads

    print('Semaphore gather')

    url = 'https://swapi.dev/api/people/{}'

    tasks = []
    # create instance of Semaphore
    sema = asyncio.Semaphore(5)

    async with aiohttp.ClientSession() as session:
        for i in range(1, 10):
            # pass Semaphore and session to every GET request
            task = fetch(sema, url.format(i), session)
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        # print(results)
        for result in results:
            print(f'{result["name"]}')
            print(f'{result["birth_year"]}')
            print(f'{result["gender"]}')

    script_time = time.time() - start_time
    print(f'The script took {script_time} second !')


if __name__ == '__main__':
    asyncio.run(main())
