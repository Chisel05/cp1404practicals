"""
Program for managing various projects, loading & storing said projects in a default or specified text file.

Estimate time: 60min
Actual time: 4hrs (cumulatively)
"""
from project import Project
import datetime

DEFAULT_FILENAME = "projects.txt"


def main():
    """Project management program with multiple features including: loading projects from a file, adding projects, updating projects, filtering projects, displaying your list of projects, and saving your list of projects"""
    print("Welcome to Pythonic Project Management")
    filename = DEFAULT_FILENAME
    projects = load_and_process_file(filename)
    print(f"Loaded {len(projects)} projects from {filename}")

    print_menu()
    option = input('>>> ').upper()
    while option != 'Q':
        if option == 'L':
            filename = input("Filename: ")
            try:
                projects = load_and_process_file(filename)
            except FileNotFoundError:
                out_file = open(filename, "w")
                out_file.close()
            print(f"Loaded {len(projects)} projects from {filename}")

        elif option == 'S':
            filename = input("Filename: ")
            save_projects(filename, projects)

        elif option == 'D':
            # Display incomplete projects, sorted by priority
            print("Incomplete projects:")
            incomplete_projects = [project for project in projects if project.completion_percentage < 100]
            incomplete_projects.sort()
            for incomplete_project in incomplete_projects:
                print(f"  {incomplete_project}")
            # Display complete projects, sorted by priority
            print("Completed projects:")
            complete_projects = [project for project in projects if project.completion_percentage == 100]
            complete_projects.sort()
            for complete_project in complete_projects:
                print(f"  {complete_project}")

        elif option == 'F':
            # Get day, month, year for search date
            day, month, year = (input("Show projects that start after date (dd/mm/yy): ").split('/'))
            # Construct search date as Date object
            search_date = datetime.date(int(year), int(month), int(day))
            # Get filtered list of projects
            filtered_projects = get_filtered_projects(projects, search_date)
            # Print list of filtered objects
            print_sorted_projects(filtered_projects)
            # for filtered_project in filtered_projects:
            #     print(filtered_project)

        elif option == 'A':
            print("Let's add a new project")
            add_new_project(projects)

        elif option == 'U':
            for i, project in enumerate(projects):
                print(i, project)
            project_choice = int(input("Project choice: "))
            print(projects[project_choice])
            try:
                new_percentage = int(input("New percentage: "))
            except ValueError:
                new_percentage = projects[project_choice].completion_percentage
            try:
                new_priority = int(input("New priority: "))
            except ValueError:
                new_priority = projects[project_choice].priority
            projects[project_choice].update_project(new_percentage, new_priority)

        else:
            print("Invalid option!")
        print_menu()
        option = input('>>> ').upper()

    save_option = input(f"Would you like to save to {filename}? ").upper()
    if save_option == 'Y':
        save_projects(filename, projects)
    print("Thank you for using custom-built project management software.")


def print_sorted_projects(projects):
    """Print list of projects in ascending order according to start date"""
    dates = [project.get_converted_start_date() for project in projects]
    dates.sort()
    for date in dates:
        for project in projects:
            if project.get_converted_start_date() == date:
                print(project)


def get_filtered_projects(projects, search_date):
    """Return filtered version of list of projects by provided date."""
    filtered_projects = []
    for project in projects:
        parts = project.start_date.split('/')
        project_date = datetime.date(int(parts[2]), int(parts[1]), int(parts[0]))
        if project_date >= search_date:
            filtered_projects.append(project)
    filtered_projects.sort()
    return filtered_projects


def save_projects(filename, projects):
    """Save list of projects (write) to specified file."""
    with open(filename, "w") as out_file:
        # Write CSV header line
        print("Name\tStart Date\tCost Estimate\tCompletion Percentage", file=out_file)
        # Write each project of projects list in correct format
        for project in projects:
            out_file.write(
                f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
        print(f"{len(projects)} saved to {DEFAULT_FILENAME}")


def add_new_project(projects):
    """Append new Project object to provided list of projects"""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost Estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def load_and_process_file(file_name):
    """Load specified file & return list of object."""
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
