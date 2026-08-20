from langgraph.graph import StateGraph, START, END

from models.vehicle_state import VehicleState

from rag.retriever import retrieve_knowledge
from rag.obd_retriever import analyze_obd_codes
from agents.symptom_agent import classify_symptom
from agents.diagnostic_agent import diagnose_vehicle
from agents.safety_agent import assess_safety
from agents.summary_agent import create_summary


# =========================================
# SYMPTOM CLASSIFICATION NODE
# =========================================

def symptom_node(state: VehicleState):

    analysis = classify_symptom(
        make=state["make"],
        model=state["model"],
        year=state["year"],
        engine=state["engine"],
        mileage=state["mileage"],
        symptom=state["symptom"],
        warning_light=state["warning_light"],
    )

    return {
        "symptom_analysis": analysis
    }

# =========================================
# OBD-II NODE
# =========================================

def obd_node(state: VehicleState):

    obd_analysis = analyze_obd_codes(
        state.get("obd_codes", "")
    )

    return {
        "obd_analysis": obd_analysis
    }
# =========================================
# RAG NODE
# =========================================

def rag_node(state: VehicleState):

    search_query = f"""
Vehicle: {state["make"]} {state["model"]}
Year: {state["year"]}
Engine: {state["engine"]}
Mileage: {state["mileage"]} km

Original symptom:
{state["symptom"]}

Structured symptom analysis:
{state["symptom_analysis"]}

Warning light:
{state["warning_light"]}

OBD-II codes:
{state.get("obd_codes", "")}

OBD-II analysis:
{state.get("obd_analysis", "")}
"""

    documents = retrieve_knowledge(
        search_query,
        top_k=3
    )

    knowledge_parts = []

    for document in documents:

        knowledge_parts.append(
            f"""
Category: {document["category"]}
Topic: {document["topic"]}

{document["text"]}
"""
        )

    knowledge = "\n\n".join(
        knowledge_parts
    )

    return {
        "retrieved_knowledge": knowledge
    }


# =========================================
# DIAGNOSTIC NODE
# =========================================

def diagnostic_node(state: VehicleState):

    diagnosis = diagnose_vehicle(
    make=state["make"],
    model=state["model"],
    year=state["year"],
    engine=state["engine"],
    mileage=state["mileage"],
    symptom=state["symptom"],
    warning_light=state["warning_light"],
    retrieved_knowledge=state["retrieved_knowledge"],
    obd_analysis=state.get(
        "obd_analysis",
        "No OBD-II analysis available."
    ),
)

    return {
        "diagnosis": diagnosis
    }


# =========================================
# SAFETY NODE
# =========================================

def safety_node(state: VehicleState):

    safety = assess_safety(
        make=state["make"],
        model=state["model"],
        year=state["year"],
        engine=state["engine"],
        mileage=state["mileage"],
        symptom=state["symptom"],
        warning_light=state["warning_light"],
    )

    return {
        "safety_assessment": safety
    }


# =========================================
# SUMMARY NODE
# =========================================

def summary_node(state: VehicleState):

    summary = create_summary(
        make=state["make"],
        model=state["model"],
        year=state["year"],
        engine=state["engine"],
        mileage=state["mileage"],
        symptom=state["symptom"],
        diagnosis=state["diagnosis"],
        safety_assessment=state["safety_assessment"],
    )

    return {
        "final_report": summary
    }


# =========================================
# CREATE GRAPH
# =========================================

graph = StateGraph(
    VehicleState
)


# =========================================
# ADD NODES
# =========================================

graph.add_node(
    "symptom",
    symptom_node
)
graph.add_node(
    "obd",
    obd_node
)

graph.add_node(
    "rag",
    rag_node
)

graph.add_node(
    "diagnostic",
    diagnostic_node
)

graph.add_node(
    "safety",
    safety_node
)

graph.add_node(
    "summary",
    summary_node
)


# =========================================
# CONNECT NODES
# =========================================

graph.add_edge(
    START,
    "symptom"
)

graph.add_edge(
    "symptom",
    "obd"
)

graph.add_edge(
    "obd",
    "rag"
)

graph.add_edge(
    "rag",
    "diagnostic"
)

graph.add_edge(
    "diagnostic",
    "safety"
)

graph.add_edge(
    "safety",
    "summary"
)

graph.add_edge(
    "summary",
    END
)


# =========================================
# COMPILE GRAPH
# =========================================

vehicle_graph = graph.compile()