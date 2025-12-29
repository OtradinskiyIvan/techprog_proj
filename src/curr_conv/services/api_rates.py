import requests
from decimal import Decimal

from curr_conv.core.converter import RateProvider
from curr_conv.core.models import ExchangeRate


class ApiRateProvider(RateProvider):
    BASE_URL = "https://api.frankfurter.app/latest"

    def get_rate(self, base: str, target: str) -> ExchangeRate:
        params = {"from": base, "to": target}
        response = requests.get(self.BASE_URL, params=params, timeout=5)
        response.raise_for_status()

        data = response.json()
        rates = data.get("rates", {})
        if target not in rates:
            raise ValueError(f"Rate {base}->{target} not found")

        rate = Decimal(str(rates[target]))
        return ExchangeRate(base, target, rate)
        return ExchangeRate(base, target, rate)
