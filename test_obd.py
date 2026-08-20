from rag.obd_retriever import analyze_obd_codes


codes = "P0301,P0171"


result = analyze_obd_codes(
    codes
)


print("\n")
print("=" * 70)
print("🚗 DRIVESENSE AI — OBD-II ANALYSIS")
print("=" * 70)

print(result)

print("=" * 70)
print("END OF OBD ANALYSIS")
print("=" * 70)