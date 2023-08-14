import requests
import json
from values import values
class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(input_text_list: list):
        if len(input_text_list) != 3:
            raise APIException('Неверное количество данных')
        else:
            base, quote, amount = input_text_list[0], input_text_list[1], input_text_list[2]

            try:
                base_ticker = values[base]
            except KeyError:
                raise APIException(f'Валюта <{base}> не найдена в списке. Для просмотра всего списка валют: /values')

            try:
                quote_ticker = values[quote]
            except KeyError:
                raise APIException(f'Валюта <{quote}> не найдена в списке. Для просмотра всего списка валют: /values')

        if base_ticker == quote_ticker:
            raise APIException('Валюты равны между собой')

        for i in amount:
            if not i.isdigit():
                raise APIException(f'Введите в конце число, а не <{amount}>')


        url = f"https://api.apilayer.com/fixer/convert?to={quote_ticker}&from={base_ticker}&amount={amount}"
        payload = {}
        headers = {"apikey": "vmLF7UdiZXNUqT7Ng0JH7ZA0y8k77ytq"}
        response = requests.request("GET", url, headers=headers, data=payload)
        response = response.text
        resp_json = json.loads(response)
        return resp_json['result']

