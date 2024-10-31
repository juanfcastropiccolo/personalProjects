import sys
import csv

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    table_format(sys.argv[1], sys.argv[2])

def table_format(input_filename, output_filename):
    try:
        with open(input_filename) as input:
            reader = csv.DictReader(input)
            rows = []
            for row in reader:
                last, first = row["name"].split(", ")
                new_row = {
                    "first": first,
                    "last": last,
                    "house": row["house"]
                }
                rows.append(new_row)

        with open(output_filename, "w") as output:
            writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])

            writer.writeheader()
            writer.writerows(rows)

    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)

if __name__ == "__main__":
    main()
