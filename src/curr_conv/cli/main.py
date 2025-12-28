import sys
from decimal import Decimal

from curr_conv.core.converter import CurrencyConverter
from curr_conv.services.local_rates import LocalRateProvider
from curr_conv.services.api_rates import ApiRateProvider


def main() -> None:
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        print("Usage: python -m curr_conv.cli.main <amount> <base> <target> [provider]")
        print("Providers: local (default), api")
        sys.exit(1)

    amount = Decimal(sys.argv[1])
    base = sys.argv[2].upper()
    target = sys.argv[3].upper()
    provider_name = sys.argv[4].lower() if len(sys.argv) == 5 else "local"

    if provider_name == "api":
        provider = ApiRateProvider()
    else:
        provider = LocalRateProvider()

    converter = CurrencyConverter(provider)
    result = converter.convert(amount, base, target)

    print(f"{amount} {base} = {result:.4f} {target}")


if __name__ == "__main__":
    main()
