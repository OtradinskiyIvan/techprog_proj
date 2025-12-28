from decimal import Decimal
from curr_conv.core.converter import RateProvider
from curr_conv.core.models import ExchangeRate


class LocalRateProvider(RateProvider):
    def __init__(self):
        self._rates = {
            ("USD", "EUR"): Decimal("0.9"),
            ("EUR", "USD"): Decimal("1.11"),
            ("USD", "RUB"): Decimal("90"),
        }

    def get_rate(self, base: str, target: str) -> ExchangeRate:
        key = (base, target)
        if key not in self._rates:
            raise ValueError(f"Rate {base}->{target} not found")

        return ExchangeRate(base, target, self._rates[key])
