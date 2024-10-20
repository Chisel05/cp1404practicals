"""
Program that reads the records of 'Wimbledon gentlemen's singles champions' as CSV, processes those records, and prints
how many times each champion has won & a list of countries that have won the competition in alphabetical order.
"""
FILENAME = 'wimbledon.csv'


def main():
    records = get_records(FILENAME)[1:]  # '[1:]' slices first processed (example) line before storing in 'records'
    name_to_championships_won = get_name_to_championships_won(records)
    print("Wimbledon Champions:")
    print_key_and_value(name_to_championships_won)

    countries = {record[3] for record in records}
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def get_records(filename):
    """Returns list of records from CSV file."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        records = [line.strip().split(",") for line in in_file]
    return records


def get_name_to_championships_won(records):
    """Iterates through record of records, adding each new name as a new key of dictionary, or incrementing key's value by 1 (if the name, as 'record[2]', is an existing key)"""
    name_to_championships_won = {}
    for record in records:
        if record[2] in name_to_championships_won:
            name_to_championships_won[record[2]] += 1  # Increment existing 'record[2]' key
        else:
            name_to_championships_won[record[2]] = 1  # New name 'record[2]' key, with value of 1
    return name_to_championships_won


def print_key_and_value(key_to_value):
    """Function that prints each key & value of that key from given dictionary"""
    for key in key_to_value:
        print(f"{key} {key_to_value[key]}")


main()
