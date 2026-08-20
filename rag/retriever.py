import faiss

from sentence_transformers import SentenceTransformer

from rag.knowledge_base import AUTOMOTIVE_KNOWLEDGE


# =========================================
# EMBEDDING MODEL
# =========================================

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# =========================================
# DOCUMENTS
# =========================================

documents = [
    item["text"]
    for item in AUTOMOTIVE_KNOWLEDGE
]


# =========================================
# EMBEDDINGS
# =========================================

embeddings = model.encode(
    documents,
    convert_to_numpy=True
)


# =========================================
# FAISS INDEX
# =========================================

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(embeddings)


# =========================================
# RETRIEVER
# =========================================

def retrieve_knowledge(
    query,
    top_k=3
):
    """
    Retrieve the most relevant automotive
    knowledge for a query.
    """

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for index_number in indices[0]:

        if index_number < len(
            AUTOMOTIVE_KNOWLEDGE
        ):

            item = AUTOMOTIVE_KNOWLEDGE[
                index_number
            ]

            results.append({
                "category": item["category"],
                "topic": item["topic"],
                "text": item["text"],
            })

    return results