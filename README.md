# Mean-Variance-Standard Deviation Calculator

## Files
- `mean_var_std.py` — contains `calculate()` implementation.
- `test_module.py` — unit tests (unittest).
- `main.py` — quick runner to print example output.

## How to run
1. Ensure NumPy is available. If not:
   ```
   pip install numpy
   ```
2. Run example:
   ```
   python3 main.py
   ```
3. Run tests:
   ```
   python3 -m unittest test_module.py
   ```

## Notes
- `calculate()` expects a list of exactly 9 numbers, otherwise raises:
  `ValueError("List must contain nine numbers.")`
- The returned dictionary values are lists (not NumPy arrays).
