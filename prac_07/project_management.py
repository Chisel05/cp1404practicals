"""
Estimate time: 60min
Actual time:
"""
from project import Project

filename = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_and_process_file(filename)
    print(f"Loaded {len(projects)} projects from {filename}")

    print_menu()
    option = input('>>> ').upper()
    while option != 'Q':
        if option == 'L':
            print("Load option")
        else:
            print("Invalid option!")
        # Get option for next loop
        print_menu()
        option = input('>>> ').upper()


def load_and_process_file(file_name):
    """Load specified file & return list of object"""
    with open(file_name, 'r') as in_file:
        projects = []
        lines = in_file.readlines()
        for line in lines[1:]:
            parts = (line.strip().split('\t'))
            # Use parts to construct & append a new Project object to projects list
            projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    return projects


def print_menu():
    """Print menu options."""
    print("- (L)oad projects"
          "\n- (S)ave projects"
          "\n- (D)isplay projects"
          "\n- (F)ilter projects by date"
          "\n- (U)pdate project"
          "\n- (Q)uit")


main()
