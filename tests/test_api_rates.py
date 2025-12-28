from decimal import Decimal
from unittest.mock import patch

from curr_conv.services.api_rates import ApiRateProvider


def test_api_rate_provider():
    fake_response = {
        "result": "success",
        "conversion_rates": {
            "EUR": 0.92
        }
    }

    with patch("curr_conv.services.api_rates.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = fake_response

        provider = ApiRateProvider()
        rate = provider.get_rate("USD", "EUR")

        assert rate.rate == Decimal("0.92")
