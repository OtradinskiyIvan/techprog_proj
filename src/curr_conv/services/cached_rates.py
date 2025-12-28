import json
from decimal import Decimal
from datetime import datetime, timedelta
from pathlib import Path

from curr_conv.core.converter import RateProvider
from curr_conv.core.models import ExchangeRate


class CachedRateProvider(RateProvider):
    def __init__(
        self,
        api_provider: RateProvider,
        cache_file: Path,
        ttl_hours: int = 24,
    ):
        self.api_provider = api_provider
        self.cache_file = cache_file
        self.ttl = timedelta(hours=ttl_hours)

    def get_rate(self, base: str, target: str) -> ExchangeRate:
        if self._cache_is_valid(base):
            return self._load_rate(base, target)

        try:
            rate = self.api_provider.get_rate(base, target)
            self._update_cache(base, rate)
            return rate
        except Exception:
            # fallback на локальный кэш
            return self._load_rate(base, target)

    # ---------- helpers ----------

    def _cache_is_valid(self, base: str) -> bool:
        if not self.cache_file.exists():
            return False

        with self.cache_file.open() as f:
            data = json.load(f)

        updated_at = datetime.fromisoformat(data["updated_at"])
        return (
            data["base"] == base
            and datetime.utcnow() - updated_at < self.ttl
        )

    def _load_rate(self, base: str, target: str) -> ExchangeRate:
        with self.cache_file.open() as f:
            data = json.load(f)

        rate = Decimal(data["rates"][target])
        return ExchangeRate(base, target, rate)

    def _update_cache(self, base: str, rate: ExchangeRate) -> None:
        data = {
            "base": base,
            "rates": {rate.target: str(rate.rate)},
            "updated_at": datetime.utcnow().isoformat(),
        }

        self.cache_file.parent.mkdir(parents=True, exist_ok=True)
        with self.cache_file.open("w") as f:
            json.dump(data, f)
