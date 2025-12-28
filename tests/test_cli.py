import subprocess
import sys


def test_cli_runs():
    result = subprocess.run(
        [sys.executable, "-m", "currency_converter.cli.main", "10", "USD", "EUR"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
