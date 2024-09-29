"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score > 100 or score < 0:
    score_category = "Invalid score"
elif score >= 90:
    score_category = "Excellent"
elif score >= 50:
    score_category = "Passable"
else:
    score_category = "Bad"
print(score_category)
