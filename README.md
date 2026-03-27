# MultiplierTest

Implements the **A & B Multiplier** PRD with a lightweight Python package equivalent:

- Generic multiplication helper (`multiply`) for multiplicative types.
- Unit tests with full line coverage target.
- Documentation content in a DocC-style folder structure.
- CI workflow that runs tests and enforces `100%` coverage.

## Quick start

1. Ensure Python 3.10+ is installed.
2. Install development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

3. Run tests:

```bash
python -m unittest discover -s tests
```

4. Run coverage (must be 100%):

```bash
python -m coverage run -m unittest discover -s tests
python -m coverage report --fail-under=100
```

## Usage

```python
from multiplier import multiply

result = multiply(6, 7)
print(result)  # 42
```
