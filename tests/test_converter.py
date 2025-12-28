import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from decimal import Decimal
from curr_conv.core.converter import CurrencyConverter
from curr_conv.services.local_rates import LocalRateProvider


def test_usd_to_eur():
    converter = CurrencyConverter(LocalRateProvider())
    result = converter.convert(Decimal("100"), "USD", "EUR")
    assert result == Decimal("90.0")

if __name__ == '__main__':
    test_usd_to_eur()
    print("Test passed!")