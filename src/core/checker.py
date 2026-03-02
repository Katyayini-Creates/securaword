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

# import re
# from src.core.feedback import generate_feedback

# def analyze_password(password: str) -> dict:

#     results = {
#         "length": len(password) >= 8,
#         "uppercase": bool(re.search(r"[A-Z]", password)),
#         "lowercase": bool(re.search(r"[a-z]", password)),
#         "digit": bool(re.search(r"[0-9]", password)),
#         "special": bool(re.search(r"[!@#$%^&*()_+=\-]", password)),
#     }

#     score = sum(results.values())

#     feedback = generate_feedback(results)

#     return {
#         "score": score,
#         "details": results,
#         "feedback": feedback
#     }

# import re
# from src.core.feedback import generate_feedback
# from src.core.entropy import calculate_entropy

# def analyze_password(password: str) -> dict:

#     results = {
#         "length": len(password) >= 8,
#         "uppercase": bool(re.search(r"[A-Z]", password)),
#         "lowercase": bool(re.search(r"[a-z]", password)),
#         "digit": bool(re.search(r"[0-9]", password)),
#         "special": bool(re.search(r"[!@#$%^&*()_+=\-]", password)),
#     }

#     score = sum(results.values())

#     entropy = calculate_entropy(password)

#     feedback = generate_feedback(results)

#     return {
#         "score": score,
#         "entropy": entropy,
#         "details": results,
#         "feedback": feedback
#     }

# import re
# from src.core.feedback import generate_feedback
# from src.core.entropy import calculate_entropy
# from src.core.attacks import is_common_password

# def analyze_password(password: str) -> dict:

#     results = {
#         "length": len(password) >= 8,
#         "uppercase": bool(re.search(r"[A-Z]", password)),
#         "lowercase": bool(re.search(r"[a-z]", password)),
#         "digit": bool(re.search(r"[0-9]", password)),
#         "special": bool(re.search(r"[!@#$%^&*()_+=\-]", password)),
#     }

#     score = sum(results.values())
#     entropy = calculate_entropy(password)
#     feedback = generate_feedback(results)

#     common = is_common_password(password)

#     if common:
#         score = 0
#         feedback.append(
#             "This password is extremely common and vulnerable to dictionary attacks."
#         )

#     return {
#         "score": score,
#         "entropy": entropy,
#         "is_common": common,
#         "details": results,
#         "feedback": feedback
#     }

# import re
# from src.core.feedback import generate_feedback
# from src.core.entropy import calculate_entropy
# from src.core.attacks import is_common_password, has_repeated_characters, has_sequential_pattern

# def analyze_password(password: str) -> dict:

#     results = {
#         "length": len(password) >= 8,
#         "uppercase": bool(re.search(r"[A-Z]", password)),
#         "lowercase": bool(re.search(r"[a-z]", password)),
#         "digit": bool(re.search(r"[0-9]", password)),
#         "special": bool(re.search(r"[!@#$%^&*()_+=\-]", password)),
#     }

#     score = sum(results.values())
#     entropy = calculate_entropy(password)
#     feedback = generate_feedback(results)

#     common = is_common_password(password)

#     if common:
#         score = 0
#         feedback.append(
#             "This password is extremely common and vulnerable to dictionary attacks."
#         )
    
#     repeated = has_repeated_characters(password)
#     sequential = has_sequential_pattern(password)

#     if repeated:
#         score = max(score - 1, 0)
#         feedback.append("Password contains repeated consecutive characters.")
    

#     if sequential:
#         score = max(score - 1, 0)
#         feedback.append("Password contains sequential patterns (e.g., 1234 or abcd).")

#     return {
#         "score": score,
#         "entropy": entropy,
#         "is_common": common,
#         "details": results,
#         "feedback": feedback
#     }

# import re
# from src.core.feedback import generate_feedback
# from src.core.entropy import calculate_entropy
# from src.core.attacks import is_common_password, has_repeated_characters, has_sequential_pattern

# def analyze_password(password: str) -> dict:

#     results = {
#         "length": len(password) >= 8,
#         "uppercase": bool(re.search(r"[A-Z]", password)),
#         "lowercase": bool(re.search(r"[a-z]", password)),
#         "digit": bool(re.search(r"[0-9]", password)),
#         "special": bool(re.search(r"[!@#$%^&*()_+=\-]", password)),
#     }

#     score = sum(results.values())
#     entropy = calculate_entropy(password)
#     feedback = generate_feedback(results)

#     common = is_common_password(password)

#     if common:
#         score = 0
#         feedback.append(
#             "This password is extremely common and vulnerable to dictionary attacks."
#         )
    
#     repeated = has_repeated_characters(password)
#     sequential = has_sequential_pattern(password)

#     if repeated:
#         score = max(score - 1, 0)
#         feedback.append("Password contains repeated consecutive characters.")
    

#     if sequential:
#         score = 0
#         feedback.append("Password contains predictable sequential patterns and is vulnerable.")

#     return {
#         "score": score,
#         "entropy": entropy,
#         "is_common": common,
#         "details": results,
#         "feedback": feedback
#     }

# import re
# from src.core.feedback import generate_feedback
# from src.core.entropy import calculate_entropy
# from src.core.attacks import is_common_password, has_repeated_characters, has_sequential_pattern

# def analyze_password(password: str) -> dict:

#     results = {
#         "length": len(password) >= 8,
#         "uppercase": bool(re.search(r"[A-Z]", password)),
#         "lowercase": bool(re.search(r"[a-z]", password)),
#         "digit": bool(re.search(r"[0-9]", password)),
#         "special": bool(re.search(r"[!@#$%^&*()_+=\-]", password)),
#     }

#     score = sum(results.values())
#     entropy = calculate_entropy(password)
#     feedback = generate_feedback(results)

#     common = is_common_password(password)

#     common = is_common_password(password)
#     repeated = has_repeated_characters(password)
#     sequential = has_sequential_pattern(password)


#     if common:
#         score = 0
#         feedback.append("This password is extremely common and vulnerable to dictionary attacks.")

#     if repeated:
#         score = 0
#         feedback.append("Password contains repeated consecutive characters and is highly predictable.")

#     if sequential:
#         score = 0
#         feedback.append("Password contains predictable sequential patterns and is vulnerable.")

#     return {
#         "score": score,
#         "entropy": entropy,
#         "is_common": common,
#         "details": results,
#         "feedback": feedback
#     }

from src.core.attacks import (
    is_common_password,
    has_repeated_characters,
    has_sequential_pattern,
    has_repeated_block,
    has_word_plus_numbers,
    has_keyboard_pattern
)
import re
from src.core.feedback import generate_feedback
from src.core.entropy import calculate_entropy

def analyze_password(password: str) -> dict:

    results = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"[0-9]", password)),
        "special": bool(re.search(r"[!@#$%^&*()_+=\-]", password)),
    }

    score = sum(results.values())
    entropy = calculate_entropy(password)
    feedback = generate_feedback(results)

    common = is_common_password(password)
    repeated = has_repeated_characters(password)
    sequential = has_sequential_pattern(password)


    if common:
        score = 0
        feedback.append("This password is extremely common and vulnerable to dictionary attacks.")

    if repeated:
        score = 0
        feedback.append("Password contains repeated consecutive characters and is highly predictable.")

    if sequential:
        score = 0
        feedback.append("Password contains predictable sequential patterns and is vulnerable.")

    repeated_block = has_repeated_block(password)
    word_number = has_word_plus_numbers(password)
    keyboard = has_keyboard_pattern(password)

    if repeated_block:
       score = 0
       feedback.append("Password is composed of repeated patterns and is predictable.")

    if word_number:
       score = 0
       feedback.append("Password follows common word + number pattern and is predictable.")

    if keyboard:
       score = 0
       feedback.append("Password contains common keyboard patterns and is vulnerable.")

    return {
        "score": score,
        "entropy": entropy,
        "is_common": common,
        "details": results,
        "feedback": feedback
    }

    

