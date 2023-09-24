"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""


name = input("Enter name: ")

print("(H)ello\n"
      "(G)oodbye\n"
      "(Q)uit")
menu_choice = input(">>> ").upper()
while menu_choice != "Q":
    if menu_choice == "H":
        print(f"Hello {name}")
    elif menu_choice == "G":
        print(f"Goodbye {name}")
    elif menu_choice == "Q":
        print()
    else:
        print("Invalid choice")
    print("(H)ello\n"
          "(G)oodbye\n"
          "(Q)uit")
    menu_choice = input(">>> ").upper()
print("Finished.")
