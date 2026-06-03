import sys

import matplotlib.pyplot

try:
    import numpy as np
    import pandas as pd
    import matplotlib
except ImportError:
    print("Missing dependencies.")
    print("Install with:")
    print("pip install -r requirements.txt")
    print("or")
    print("poetry install")
    sys.exit(1)

print("LOADING STATUS: Loading programs...")
print("Checking dependencies:")
print(f"[OK] pandas ({pd.__version__})")
print(f"[OK] numpy ({np.__version__})")
print(f"[OK] matplotlib ({matplotlib.__version__})")
print()
print("pip uses requirements.txt")
print("Poetry uses pyproject.toml")
print()
print("Analyzing Matrix data ...")

rng = np.random.default_rng(42)

df = pd.DataFrame({
    "time": np.arange(1000),
    "signal": rng.normal(50, 12, 1000)
})

print(f"Processing {len(df)} data points...")

matplotlib.pyplot.plot(df["time"], df["signal"])
matplotlib.pyplot.title("Matrix Signal Strength")
matplotlib.pyplot.savefig("matrix_analysis.png")
matplotlib.pyplot.close()

print("Analysis complete!")
print("Results saved to: matrix_analysis.png")
