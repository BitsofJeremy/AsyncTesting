## Future Python programming with Asyncio

A set of examples for using Asyncio to get information from an API.

Using the Starwars API as an example: https://swapi.dev/documentation

### Setup

*Requires Python 3.7.5+*

Clone the repo

	git clone https://gitlab.com/deafmice/asynctesting.git

Create and source a virtualenv

	virtualenv -p python venv
	source venv/bin/activate

Install the things with pip

	pip install -r requirements.txt



### Run

Original Requests Module

	python og_requests_way.py

Asyncio with as_completed

	python async_as_completed.py

Asyncio with gather

	python async_gather.py

Asyncio with Semaphore as completed

	python async_semaphore_as_completed.py	

Asyncio with Semaphore gathered

	python async_semaphore_gather.py	

### References

 - https://www.integralist.co.uk/posts/python-asyncio/
 - https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html
 - https://stackoverflow.com/questions/56523043/using-python-3-7-to-make-100k-api-calls-making-100-in-parallel-using-asyncio
 - https://stackoverflow.com/questions/40836800/python-asyncio-semaphore-in-async-await-function

