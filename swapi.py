import requests
from pathlib import Path


class APIRequester:
    def __init__(self, base_url='https://www.swapi.tech/api'):
        self.base_url = base_url.rstrip('/')

    def get(self, url):
        try:
            response = requests.get(self.base_url + url)
            response.raise_for_status()
            return response
        except requests.ConnectionError as e:
            print(f'Произошла ошибка соединения с {self.base_url}')
            print(f'Ошибка соединения: {e}')
        except requests.RequestException:
            print('Возникла ошибка при выполнении запроса')


class SWRequester(APIRequester):
    def get_sw_categories(self):
        try:
            response = requests.get(self.base_url.rstrip('/') + '/')
            response.raise_for_status()
            categories = response.json()
            return categories.keys()
        except requests.ConnectionError as e:
            print(f'Произошла ошибка соединения с {self.base_url}')
            print(f'Ошибка соединения: {e}')
        except requests.RequestException:
            print('Возникла ошибка при выполнении запроса')

    def get_sw_info(self, sw_type):
        try:
            response = requests.get(f'{self.base_url}/{sw_type}/')
            response.raise_for_status()
            return response.text
        except requests.ConnectionError as e:
            print(f'Произошла ошибка соединения с {self.base_url}')
            print(f'Ошибка соединения: {e}')
        except requests.RequestException:
            print('Возникла ошибка при выполнении запроса')


def save_sw_data(base_url='https://swapi.dev/api'):
    directory = Path('data')
    directory.mkdir(exist_ok=True)
    requester = SWRequester(base_url)
    requester.get_sw_categories()
    for category in requester.get_sw_categories():
        file_path = f'data/{category}.txt'
        with open(file_path, 'w') as file:
            data = requester.get_sw_info(category)
            file.write(data)
