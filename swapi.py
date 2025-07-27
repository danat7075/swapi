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
        category_dict = {}
        response = self.get('/')
        response.raise_for_status()
        categories = response.json()
        if 'result' in categories and response.status_code == 200:
            for category, url in categories['result'].items():
                category_dict[category] = url
            return category_dict.keys()
        else:
            print("Ключ 'result' не найден в ответе.")
            return categories.keys()

    def get_sw_info(self, sw_type):
        response = self.get(f'/{sw_type}/')
        response.raise_for_status()
        return response.text


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