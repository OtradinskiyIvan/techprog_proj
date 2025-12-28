# Currency Converter
This is a currency converter with support for local exchange rates and API updates, implemented as a Python package with a CLI.
The project includes testing, Git Flow, and CI.

Key Features:

- Currency conversion using local exchange rates
- Automatic updating of local rates via API
- Support for multiple rate sources: local and online (API)
- CLI for use in the terminal

Project Structure:

- core — contains CurrencyConverter and the RateProvider interface
- services — implementations of rate providers:
  - LocalRateProvider — local exchange rates
  - ApiRateProvider — external API
  - CachedRateProvider — automatic updating of local rates via API
  - cli — command line interface, accepts arguments: <amount> <base> <target> [local|api]

This project is currently under development.

## Roadmap:
- ✅ Create an offline currency converter (local rates)
- ✅ Create currency converter using API
- ✅ Autoupdate info in offline converter using API (cached provider)

## Installation

1. Clone the repository.
2. Install dependencies: `python -m pip install -r requirements.txt`
3. Install the package in development mode: `python -m pip install -e .`

## Usage

Run the CLI converter with local rates (default):

```bash
py -m curr_conv.cli.main 100 USD EUR
```

Or with live API rates:

```bash
py -m curr_conv.cli.main 100 USD EUR api
```

Or with cached API rates (updates every 24 hours):

```bash
py -m curr_conv.cli.main 100 USD EUR cached
```

## Running Tests

```bash
pytest
```
