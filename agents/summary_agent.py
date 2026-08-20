from utils.llm import llm


def create_summary(
    make,
    model,
    year,
    engine,
    mileage,
    symptom,
    diagnosis,
    safety_assessment,
):
    """
    Combine the diagnostic and safety assessments
    into one user-friendly report.
    """

    prompt = f"""
You are the final reporting agent for DriveSense AI.

Your job is to combine a vehicle diagnosis and a
safety assessment into one clear report for the
vehicle owner.

VEHICLE:

Make: {make}
Model: {model}
Year: {year}
Engine: {engine}
Mileage: {mileage} km

SYMPTOM:

{symptom}

DIAGNOSTIC ANALYSIS:

{diagnosis}

SAFETY ASSESSMENT:

{safety_assessment}

Create a concise but useful final report.

Use this structure:

# 🚗 DriveSense AI Report

## Vehicle

Summarize the vehicle.

## 🔧 Reported Problem

Summarize the user's complaint.

## 🔍 Possible Causes

Summarize the most likely causes from
the diagnostic analysis.

Do NOT claim that any cause is confirmed.

## 🛠️ Recommended Checks

List the checks in priority order.

## 🚨 Safety Assessment

Clearly show the safety level and
driving recommendation.

## 👨‍🔧 When to See a Mechanic

Explain when professional inspection
is recommended.

## ❓ Important Follow-up Questions

List the most useful unanswered questions.

IMPORTANT:

DriveSense AI provides guidance, not a confirmed
mechanical diagnosis. Encourage professional
inspection where appropriate.
"""

    response = llm.invoke(prompt)

    return response.content