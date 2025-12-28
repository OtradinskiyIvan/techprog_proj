# Currency Converter

This project is currently under development.

## Roadmap:
- ✅ Create an offline currency converter (local rates)
- ✅ Create currency converter using API
- Autoupdate info in offline converter using API

## Installation

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Install the package in development mode: `pip install -e .`

## Usage

Run the CLI converter with local rates (default):

```bash
py -m curr_conv.cli.main 100 USD EUR
```

Or with live API rates:

```bash
py -m curr_conv.cli.main 100 USD EUR api
```

## Running Tests

```bash
pytest
```