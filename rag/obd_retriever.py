from rag.obd_database import OBD_DATABASE


def analyze_obd_codes(
    obd_codes
):
    """
    Analyze OBD-II codes using the local
    DriveSense AI OBD database.
    """

    if not obd_codes:
        return "No OBD-II codes were provided."

    # -----------------------------------------
    # CLEAN USER INPUT
    # -----------------------------------------

    codes = [
        code.strip().upper()
        for code in obd_codes.split(",")
        if code.strip()
    ]

    results = []

    # -----------------------------------------
    # LOOK UP CODES
    # -----------------------------------------

    for code in codes:

        if code in OBD_DATABASE:

            data = OBD_DATABASE[code]

            causes = "\n".join(
                f"- {cause}"
                for cause in data["possible_causes"]
            )

            result = f"""
OBD-II Code: {code}

Description:
{data["description"]}

System:
{data["system"]}

Possible Causes:
{causes}

Important:
This code does not by itself confirm which
physical component has failed. Additional
diagnostic testing is required.
"""

            results.append(result)

        else:

            results.append(
                f"""
OBD-II Code: {code}

DriveSense AI does not currently have this
code in its local database.

The code should be checked against reliable
vehicle-specific diagnostic information.
"""
            )

    return "\n\n".join(results)