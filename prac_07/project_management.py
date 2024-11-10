"""
Estimate time: 60min
Actual time:
"""
from project import Project
import datetime

FILENAME = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_and_process_file(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    print_menu()
    option = input('>>> ').upper()
    while option != 'Q':
        if option == 'L':
            filename = input("Filename: ")
            projects = load_and_process_file(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif option == 'S':
            filename = input("Filename: ")
            with open(filename, "w") as out_file:
                # Write CSV header line
                print("Name\tStart Date\tCost Estimate\tCompletion Percentage", file=out_file)
                # Write each project of projects list in correct format
                for project in projects:
                    out_file.write(
                        f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
                print(f"{len(projects)} saved to {FILENAME}")
        elif option == 'D':
            # Display incomplete projects, sorted by date
            print("Incomplete projects:")
            incomplete_projects = [project for project in projects if project.completion_percentage < 100]
            incomplete_projects.sort()
            for incomplete_project in incomplete_projects:
                print(incomplete_project)
            # Display complete projects, sorted by date
            print("Completed projects:")
            complete_projects = [project for project in projects if project.completion_percentage == 100]
            complete_projects.sort()
            for complete_project in complete_projects:
                print(complete_project)
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
