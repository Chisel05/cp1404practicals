"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}

print(CODE_TO_NAME)
state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

for state_code in CODE_TO_NAME:  # 'state_code' variable repurposed as iteration variable for loop & no longer used for user input
    print(
        f"{state_code:3} is {CODE_TO_NAME[state_code]:28}")  # Chose not to use dynamic spacing, since it's unlikely that new states will be added or exiting states removed
