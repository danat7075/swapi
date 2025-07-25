import requests
import os

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
        category_dict = {}  
        try:
            response = requests.get(f'{self.base_url}/{endpoint}')
            response.raise_for_status()
            categories = response.json()
            for category,url in categories['result'].items():
                category_dict[category] = url
            return category_dict.keys()
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
            return response.text
        except requests.ConnectionError as e:
            print(f'Произошла ошибка соединения с {self.base_url}')
            print(f'Ошибка соединения: {e}')
        except requests.RequestException as e:
            print(f'Произошла ошибка запроса с {self.base_url}')
            print(f'Ошибка запроса: {e}')
    
def save_sw_data(base_url='https://www.swapi.tech/api'):
    directory = 'data'
    if not os.path.exists(directory):
        os.makedirs(directory)
    requester = SWRequester(base_url)
    requester.get_sw_categories()
    for category in requester.get_sw_categories():
        file_path = os.path.join(directory, f'{category}.txt')
        with open(file_path, 'w') as file:
            data = requester.get_sw_info(category)
            file.write(data)

#api_requester = SWRequester()

# Пример использования метода get_sw_info для получения информации о людях
"""people_info = api_requester.get_sw_categories()
print(people_info)  # Печатаем весь ответ, который будет строкой"""
"""response = requests.get('https://www.swapi.tech/api')
response.raise_for_status()
categories = response.json()
print(categories)  # Печатаем весь ответ, который будет словарем"""

save_sw_data()