"""
Estimate time: 60min
Actual time:
"""
from project import Project


def main():
    print("MENU:"
          "\n(L)oad projects")
    option = input('>>> ')
    while option != '':
        if option == 'L':
            print("Load option")
        else:
            print("Invalid option!")
        # Get option for next loop
        print("MENU:"
              "\n(L)oad projects")
        option = input('>>> ')


main()
