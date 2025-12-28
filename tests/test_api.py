import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from decimal import Decimal
from curr_conv.core.converter import CurrencyConverter
from curr_conv.services.api_rates import ApiRateProvider


def test_api_usd_to_eur():
    converter = CurrencyConverter(ApiRateProvider())
    result = converter.convert(Decimal("100"), "USD", "EUR")
    print(f"100 USD = {result} EUR")
    assert result > 0  # Простая проверка, что результат положительный


if __name__ == '__main__':
    test_api_usd_to_eur()
    print("API test passed!")