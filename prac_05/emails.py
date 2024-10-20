"""
Word Occurrences
Estimate: 15 minutes
Actual:   25 minutes
"""

emails = []
name_to_email = {}
email = input("Email: ")
while email != "":
    emails.append(email)
    name = email.split("@")[0].split(".")
    name = " ".join(name).title()
    name_confirmation = input(f"Is your name {name}? (Y/n) ").lower()
    if name_confirmation == "n":
        name = input("Name: ").title()
    name_to_email[name] = email
    email = input("Email: ")

print()
for name in name_to_email:
    print(f"{name} ({name_to_email[name]})")
