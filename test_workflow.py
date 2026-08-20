from coordinator import vehicle_graph


initial_state = {
    "make": "Toyota",
    "model": "Corolla",
    "year": 2018,
    "engine": "1.6L Petrol",
    "mileage": 120000,
    "symptom": """
My car shakes when I press the accelerator.
Sometimes it feels like it loses power.
The problem happens mostly when I accelerate
from a stop. The Check Engine Light is on.
""",
    "warning_light": "Check Engine Light",
    "obd_codes": "P0301,P0171",
}


result = vehicle_graph.invoke(initial_state)


print("\n")
print("=" * 70)
print("🚗 DRIVESENSE AI MULTI-AGENT REPORT")
print("=" * 70)
print("\n")

print(result["final_report"])

print("\n")
print("=" * 70)
print("END OF REPORT")
print("=" * 70)