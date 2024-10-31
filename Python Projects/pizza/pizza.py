import sys
import tabulate
import csv

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    if not sys.argv[1].endswith("csv"):
        print("Not a CSV File")
        sys.exit(1)

    table_format(sys.argv[1])

def table_format(filename):
    try:
        with open(filename) as csv_file:
            reader = csv.reader(csv_file)
            datos = list(reader)

            new_table = tabulate.tabulate(datos, headers="firstrow", tablefmt="grid")
            print(new_table)

    except FileNotFoundError:
        print(f"Could not read {filename}")
        sys.exit(1)

if __name__ == "__main__":
    main()


