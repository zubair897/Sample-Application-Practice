import sys

print("🤖 AI validation running...")

with open("Dockerfile") as f:
    data = f.read()

if "FROM" not in data:
    print("❌ Dockerfile invalid")
    sys.exit(1)

print("✅ AI validation passed")
