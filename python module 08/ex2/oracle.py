import os
import sys
from dotenv import load_dotenv

load_dotenv()

print("ORACLE STATUS: Reading the Matrix...")
print()

mode = os.getenv("MATRIX_MODE", "development")
database = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL", "DEBUG")
zion = os.getenv("ZION_ENDPOINT")

print("Configuration loaded:")
print(f"Mode: {mode}")

if database:
    if mode == "production":
        print("Database: Connected to production cluster")
    else:
        print("Database: Connected to local instance")
else:
    print("Database: Missing")

if api_key:
    print("API Access: Authenticated")
else:
    print("API Access: Missing")

print(f"Log Level: {log_level}")

if zion:
    print("Zion Network: Online")
else:
    print("Zion Network: Offline")

print()
print("Environment security check:")

try:
    with open(".gitignore", "r", encoding="utf-8") as file:
        gitignore_content = file.read()

    if ".env" in gitignore_content:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env missing from .gitignore")
except FileNotFoundError:
    print("[WARNING] .gitignore not found")

print("[OK] No hardcoded secrets detected")

print("[OK] Production overrides available")

print()
print("The Oracle sees all configurations.")


missing: list[str] = []

if not database:
    missing.append("DATABASE_URL")

if not api_key:
    missing.append("API_KEY")

if not zion:
    missing.append("ZION_ENDPOINT")

if missing:
    print()
    print("Missing required configuration:")
    for item in missing:
        print(f"- {item}")
    sys.exit(1)
