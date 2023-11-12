import aiohttp
import asyncio
import time


async def fetch(session, url):
    # Get the goods
    async with session.get(url) as response:
        return await response.json()


async def main():
    start_time = time.time()

    # ##################################################
    # This prints results after they are done

    print('Async gather')

    url = 'https://swapi.dev/api/people/{}'

    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(1, 10):
            tasks.append(fetch(session, url.format(i)))

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
