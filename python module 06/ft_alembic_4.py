import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print("Now show that not all functions can be reached")
print("This will raise an exception!")
try:
    print(f"Testing the hidden create_earth: {alchemy.create_earth()}") # type: ignore
except Exception as e:
    import traceback
    import sys
    traceback.print_exc(file=sys.stdout)
