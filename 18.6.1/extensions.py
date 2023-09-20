import requests
import json
from config import keys


class ConversionException(Exception):
    pass


class PairConvetor():
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        # values = message.text.split(' ')
        # quote, base, ammount = values
        
        if quote == base:
            raise ConversionException('Нельзя конвертировать одинаковые валюты')
    
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'Не удалось обработать  валюту: {quote}')
    
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'Не удалось обработать  валюту: {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Не удалось обработать  количество: {amount}')
        
        r = requests.get(f'https://min-api-v2.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        total_base_sum = total_base*amount

        return total_base_sum
