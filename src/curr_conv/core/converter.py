from decimal import Decimal
from curr_conv.core.models import ExchangeRate


class RateProvider:
    def get_rate(self, base: str, target: str) -> ExchangeRate:
        raise NotImplementedError


class CurrencyConverter:
    def __init__(self, rate_provider: RateProvider):
        self.rate_provider = rate_provider

    def convert(self, amount: Decimal, base: str, target: str) -> Decimal:
        rate = self.rate_provider.get_rate(base, target)
        return amount * rate.rate
