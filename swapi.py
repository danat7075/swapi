import requests
from bs4 import BeautifulSoup

class APIRequester:
    def __init__(self, base_url='https://www.swapi.tech/api'):
        self.base_url = base_url

    def get(self, endpoint=''):
        try:
            response = requests.get(f'{self.base_url}/{endpoint}')
            response.raise_for_status()
            return response.json()
        except requests.ConnectionError as e:
            print(f'Произошла ошибка соединения с {self.base_url}')
            print(f'Ошибка соединения: {e}')
        except requests.RequestException as e:
            print(f'Произошла ошибка запроса с {self.base_url}')
            print(f'Ошибка запроса: {e}')

class SWRequester(APIRequester):
    def __init__(self, base_url='https://www.swapi.tech/api'):
        super().__init__(base_url)


    def get_sw_categories(self, endpoint=''):
        try:
            response = requests.get(f'{self.base_url}/{endpoint}')
            response.raise_for_status()
            categories = response.json()
            print("Доступные категории:")
            for category in categories['result']:
                print(category)
        except requests.ConnectionError as e:
            print(f'Произошла ошибка соединения с {self.base_url}')
            print(f'Ошибка соединения: {e}')
        except requests.RequestException as e:
            print(f'Произошла ошибка запроса с {self.base_url}')
            print(f'Ошибка запроса: {e}')

    def get_sw_info(self, sw_type):
        try:
            response = requests.get(f'{self.base_url}/{sw_type}')
            response.raise_for_status()
            return f'Результат категории {sw_type}: \n{response.text}'
        except requests.ConnectionError as e:
            print(f'Произошла ошибка соединения с {self.base_url}')
            print(f'Ошибка соединения: {e}')
        except requests.RequestException as e:
            print(f'Произошла ошибка запроса с {self.base_url}')
            print(f'Ошибка запроса: {e}')
    


api_requester = SWRequester()

# Пример использования метода get_sw_info для получения информации о людях
people_info = api_requester.get_sw_info("people")
print(people_info)  # Печатаем весь ответ, который будет строкой
