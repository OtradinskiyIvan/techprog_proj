from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class ExchangeRate:
    base: str
    target: str
    rate: Decimal
