import requests
from decimal import Decimal

from curr_conv.core.converter import RateProvider
from curr_conv.core.models import ExchangeRate


class ApiRateProvider(RateProvider):
    API_KEY = "56d4994a5c2a39a2b2f07ff5"
    BASE_URL = "https://v6.exchangerate-api.com/v6/{api_key}/latest/{base}"

    def get_rate(self, base: str, target: str) -> ExchangeRate:
        url = self.BASE_URL.format(api_key=self.API_KEY, base=base)

        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        if data.get("result") != "success":
            raise ValueError("API error while fetching exchange rates")

        rates = data.get("conversion_rates", {})
        if target not in rates:
            raise ValueError(f"Rate {base}->{target} not found")

        rate = Decimal(str(rates[target]))
        return ExchangeRate(base, target, rate)
