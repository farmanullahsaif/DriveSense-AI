from agents.safety_agent import assess_safety


result = assess_safety(
    make="Toyota",
    model="Corolla",
    year=2018,
    engine="1.6L Petrol",
    mileage=120000,
    symptom="My car is jerking while accelerating.",
    warning_light="Check Engine Light",
)


print("\n")
print("=" * 60)
print("DRIVESENSE AI SAFETY ASSESSMENT")
print("=" * 60)
print("\n")

print(result)

print("\n")
print("=" * 60)
print("END OF SAFETY ASSESSMENT")
print("=" * 60)