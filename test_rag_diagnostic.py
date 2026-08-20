from agents.diagnostic_agent import diagnose_vehicle


result = diagnose_vehicle(
    make="Toyota",
    model="Corolla",
    year=2018,
    engine="1.6L Petrol",
    mileage=120000,
    symptom="My car is jerking while accelerating.",
    warning_light="Check Engine Light",
)


print("\n")
print("=" * 70)
print("🚗 DRIVESENSE AI — RAG DIAGNOSTIC TEST")
print("=" * 70)
print("\n")

print(result)

print("\n")
print("=" * 70)
print("END OF TEST")
print("=" * 70)