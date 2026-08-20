from typing import TypedDict


class VehicleState(TypedDict, total=False):

    # -----------------------------------------
    # VEHICLE INFORMATION
    # -----------------------------------------

    make: str
    model: str
    year: int
    engine: str
    mileage: int

    # -----------------------------------------
    # USER PROBLEM
    # -----------------------------------------

    symptom: str
    warning_light: str
    # -----------------------------------------
    # OBD-II
    # -----------------------------------------

    obd_codes: str
    obd_analysis: str
    # -----------------------------------------
    # SYMPTOM ANALYSIS
    # -----------------------------------------

    symptom_category: str
    primary_symptom: str
    secondary_symptoms: str
    operating_conditions: str
    symptom_severity: str
    symptom_analysis: str

    # -----------------------------------------
    # RAG
    # -----------------------------------------

    retrieved_knowledge: str

    # -----------------------------------------
    # AGENT OUTPUTS
    # -----------------------------------------

    diagnosis: str
    safety_assessment: str
    final_report: str