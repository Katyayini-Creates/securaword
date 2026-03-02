# from src.core.checker import analyze_password

# def classify(score: int) -> str:
#     if score == 5:
#         return "Strong 💪"
#     elif score >= 3:
#         return "Medium ⚠️"
#     else:
#         return "Weak ❌"

# if __name__ == "__main__":
#     password = input("Enter your password: ")

#     result = analyze_password(password)
#     strength = classify(result["score"])

#     print("\nPassword Analysis:")
#     print("Strength:", strength)
#     print("Details:", result["details"])

# from src.core.checker import analyze_password

# def classify(score: int) -> str:
#     if score == 5:
#         return "Strong 💪"
#     elif score >= 3:
#         return "Medium ⚠️"
#     else:
#         return "Weak ❌"

# if __name__ == "__main__":
#     password = input("Enter your password: ")

#     result = analyze_password(password)
#     strength = classify(result["score"])

#     print("\nPassword Analysis:")
#     print("Strength:", strength)

#     if result["feedback"]:
#         print("\nSuggestions:")
#         for item in result["feedback"]:
#             print("-", item)

# from src.core.checker import analyze_password

# def classify(score: int) -> str:
#     if score == 5:
#         return "Strong 💪"
#     elif score >= 3:
#         return "Medium ⚠️"
#     else:
#         return "Weak ❌"

# if __name__ == "__main__":
#     password = input("Enter your password: ")

#     result = analyze_password(password)
#     strength = classify(result["score"])

#     print("\nPassword Analysis:")
#     print("Strength:", strength)
#     print("Entropy (bits):", result["entropy"])

#     if result["feedback"]:
#         print("\nSuggestions:")
#         for item in result["feedback"]:
#             print("-", item)


# from src.core.checker import analyze_password

# def classify(score: int) -> str:
#     if score == 5:
#         return "Strong 💪"
#     elif score >= 3:
#         return "Medium ⚠️"
#     else:
#         return "Weak ❌"

# if __name__ == "__main__":
#     password = input("Enter your password: ")

#     result = analyze_password(password)
#     strength = classify(result["score"])

#     print("\nPassword Analysis:")
#     print("Strength:", strength)
#     print("Entropy (bits):", result["entropy"])

#     if result["is_common"]:
#         print("⚠ WARNING: This password appears in common password lists!")

#     if result["feedback"]:
#         print("\nSuggestions:")
#         for item in result["feedback"]:
#             print("-", item)

from src.core.checker import analyze_password

def classify(score: int, entropy: float) -> str:
    """
    Classify password strength based on score and entropy.
    """

    if score == 0:
        return "Very Weak ❌"

    if entropy < 28:
        return "Weak ⚠️"

    if entropy < 50:
        return "Moderate 🔐"

    if entropy < 80:
        return "Strong 💪"

    return "Very Strong 🚀"

if __name__ == "__main__":
    password = input("Enter your password: ")

    result = analyze_password(password)
    strength = classify(result["score"], result["entropy"])

    print("\n" + "="*40)
print("        SECURAWORD ANALYSIS")
print("="*40)

print(f"Strength        : {strength}")
print(f"Entropy (bits)  : {result['entropy']}")
print(f"Score           : {result['score']} / 5")

if result["feedback"]:
    print("\nSuggestions:")
    for item in result["feedback"]:
        print(f" - {item}")

print("="*40)

