import sys

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    if not sys.argv[1].endswith("py"):
        print("Not a Python File")
        sys.exit(1)

    count_lines(sys.argv[1])

def count_lines(filename):
    lines_counter = 0

    try:
        with open(filename) as file:
            lines = file.readlines()
            for line in lines:
                stripped_line = line.strip()
                if stripped_line == "" or stripped_line.startswith("#"):
                    continue
                else:
                    lines_counter += 1
            print(lines_counter)

    except FileNotFoundError:
        print(f"Could not read {filename}")
        sys.exit(1)


if __name__ == "__main__":
    main()
