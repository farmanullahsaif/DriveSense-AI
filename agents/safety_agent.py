from utils.llm import llm


def assess_safety(
    make,
    model,
    year,
    engine,
    mileage,
    symptom,
    warning_light,
):
    """
    Assess the urgency and safety risk associated
    with the reported vehicle problem.
    """

    prompt = f"""
You are the Safety Agent for DriveSense AI.

Your ONLY responsibility is to evaluate the potential
safety risk of a reported vehicle problem.

You are NOT responsible for giving a final mechanical
diagnosis.

VEHICLE:

Make: {make}
Model: {model}
Year: {year}
Engine: {engine}
Mileage: {mileage} km

REPORTED SYMPTOM:

{symptom}

WARNING LIGHT:

{warning_light}

Classify the situation into exactly ONE of these levels:

LOW
MEDIUM
HIGH

Meaning:

LOW:
No obvious immediate safety threat based on the
information provided.

MEDIUM:
The vehicle may be unsafe or could suffer further
damage. Professional inspection is recommended.

HIGH:
The vehicle may be dangerous to drive.
The user should stop driving and seek professional
assistance.

IMPORTANT:

- Do not claim certainty.
- Base the assessment only on the information provided.
- If critical information is missing, mention it.
- Never encourage the user to perform dangerous repairs.
- When in doubt about a potentially dangerous symptom,
  recommend professional inspection.

Return the response using this exact structure:

## 🚨 Safety Assessment

Risk Level: LOW / MEDIUM / HIGH

## ⚠️ Why

Explain why this risk level was selected.

## 🚗 Driving Recommendation

Explain whether the user should:

- Continue driving normally
- Drive only a short distance to a mechanic
- Stop driving and arrange professional assistance

## 🛑 Immediate Stop Conditions

List symptoms that mean the user should stop driving
immediately.

## 🔧 Safe Next Action

Give the safest next step for the user.
"""

    response = llm.invoke(prompt)

    return response.content