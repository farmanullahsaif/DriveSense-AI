from utils.llm import llm


def classify_symptom(
    make,
    model,
    year,
    engine,
    mileage,
    symptom,
    warning_light,
):
    """
    Convert a user's natural-language vehicle complaint
    into structured symptom information.
    """

    prompt = f"""
You are the Symptom Classification Agent for DriveSense AI.

Your job is to analyze a vehicle owner's description
and convert it into structured automotive symptom
information.

Do NOT diagnose the mechanical problem.

Do NOT claim that a component has failed.

Only classify and describe the symptoms.

VEHICLE:

Make: {make}
Model: {model}
Year: {year}
Engine: {engine}
Mileage: {mileage} km

USER DESCRIPTION:

{symptom}

WARNING LIGHT:

{warning_light}

Classify the complaint using:

## Symptom Category

Choose the most appropriate category, such as:

- Engine / Drivability
- Transmission
- Braking
- Steering
- Suspension
- Electrical
- Cooling
- Fuel System
- Exhaust
- Starting
- Other

## Primary Symptom

Identify the main complaint.

## Secondary Symptoms

Identify additional symptoms if present.

## Operating Conditions

Describe when the symptom occurs.

Examples:

- During acceleration
- During braking
- At idle
- During cold start
- At high speed
- During gear changes
- Constantly
- Intermittently

## Symptom Severity

Classify as:

LOW
MEDIUM
HIGH

This is a symptom severity classification,
not a confirmed safety assessment.

## Symptom Analysis

Briefly explain what the user appears
to be experiencing.

Return the information clearly.
"""

    response = llm.invoke(prompt)

    return response.content