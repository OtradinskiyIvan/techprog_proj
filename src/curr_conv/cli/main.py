import sys
from decimal import Decimal

from curr_conv.core.converter import CurrencyConverter
from curr_conv.services.local_rates import LocalRateProvider


def main() -> None:
    if len(sys.argv) != 4:
        print("Usage: python -m curr_conv.cli.main <amount> <base> <target>")
        sys.exit(1)

    amount = Decimal(sys.argv[1])
    base = sys.argv[2].upper()
    target = sys.argv[3].upper()

    converter = CurrencyConverter(LocalRateProvider())
    result = converter.convert(amount, base, target)

    print(f"{amount} {base} = {result:.2f} {target}")


if __name__ == "__main__":
    main()
