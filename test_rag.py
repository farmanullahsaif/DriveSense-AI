from rag.retriever import retrieve_knowledge


query = """
Toyota Corolla is jerking during acceleration
and the Check Engine Light is on.
"""


results = retrieve_knowledge(
    query,
    top_k=3
)


print("\n")
print("=" * 70)
print("🚗 DRIVESENSE AI — RETRIEVED AUTOMOTIVE KNOWLEDGE")
print("=" * 70)


for number, result in enumerate(results, start=1):

    print(f"\n--- RESULT {number} ---\n")

    print(result)


print("\n")
print("=" * 70)
print("END OF RETRIEVAL")
print("=" * 70)