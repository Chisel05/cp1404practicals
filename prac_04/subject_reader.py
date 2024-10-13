"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subjects(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line_parts = line.strip().split(',')
        line_parts[2] = int(line_parts[2])
        data.append(line_parts)
    input_file.close()
    return data


def display_subjects(data):
    for subject in range(len(data)):
        subject_parts = data[subject]
        print(f"{subject_parts[0]} is taught by {subject_parts[1]} and has {subject_parts[2]} students")


main()
