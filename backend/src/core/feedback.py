def generate_feedback(results: dict) -> list:
    """
    Generate improvement suggestions
    based on which rules failed.
    """

    feedback = []

    if not results["length"]:
        feedback.append("Password should be at least 8 characters long.")

    if not results["uppercase"]:
        feedback.append("Add at least one uppercase letter (A-Z).")

    if not results["lowercase"]:
        feedback.append("Add at least one lowercase letter (a-z).")

    if not results["digit"]:
        feedback.append("Include at least one number (0-9).")

    if not results["special"]:
        feedback.append("Include at least one special character (!@#$ etc).")

    return feedback