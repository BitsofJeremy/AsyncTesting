import requests
import time


def main():
    start_time = time.time()

    # ##################################################
    # This prints results after they are done

    print('OG requests way')

    url = 'https://swapi.dev/api/people/{}'

    for i in range(1, 10):
        response = requests.get(url=url.format(i))
        data = response.json()
        print(f'{data["name"]}')
        print(f'{data["birth_year"]}')
        print(f'{data["gender"]}')

    script_time = time.time() - start_time
    print(f'The script took {script_time} second !')


if __name__ == '__main__':
    main()
