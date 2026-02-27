# import re

# def analyze_password(password: str) -> dict:
#     """
#     Analyze password strength using basic security rules.
#     Returns a dictionary with score and rule results.
#     """

#     results = {
#         "length": len(password) >= 8,
#         "uppercase": bool(re.search(r"[A-Z]", password)),
#         "lowercase": bool(re.search(r"[a-z]", password)),
#         "digit": bool(re.search(r"[0-9]", password)),
#         "special": bool(re.search(r"[!@#$%^&*()_+=\-]", password)),
#     }

#     score = sum(results.values())

#     return {
#         "score": score,
#         "details": results
#     }

import re
from src.core.feedback import generate_feedback

def analyze_password(password: str) -> dict:

    results = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"[0-9]", password)),
        "special": bool(re.search(r"[!@#$%^&*()_+=\-]", password)),
    }

    score = sum(results.values())

    feedback = generate_feedback(results)

    return {
        "score": score,
        "details": results,
        "feedback": feedback
    }