"""
REQUIREMENTS:
list of lists = 1
sets = 1
dictionaries = 1
functions = 4 (including main)
& final output done using '.join()' string method

WHAT I HAVE:
lists = 1, records_data
sets = 2, names & countries (ONE OVER!)
dictionaries = 1, name_to_championships_won
functions = 2, main() & get_records_data()
& final output uses '.join()' string method

TO BE DONE:
- eliminate (1) set without sacrificing functionality
- refactor main into (2) extra functions
"""
FILENAME = 'wimbledon.csv'


def main():
    records_data = get_records_data(FILENAME)

    names = {line_data[2] for line_data in records_data[1:]}

    name_to_championships_won = {}
    for name in names:
        for line_data in records_data:
            if line_data[2] == name:
                if name in name_to_championships_won:
                    name_to_championships_won[name] += 1
                else:
                    name_to_championships_won[name] = 1

    print("Wimbledon Champions:")
    for name in name_to_championships_won:
        print(f"{name} {name_to_championships_won[name]}")

    countries = {line_data[3] for line_data in records_data[1:]}
    countries = sorted([country for country in countries])
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def get_records_data(filename):
    records_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            records_data.append(line.strip().split(","))
    return records_data


main()
