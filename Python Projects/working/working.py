import re



def main():
    print(convert(input("Hours: ")))

def convert(time_frame):
    pattern = r"(\d{1,2}:?\d{0,2}) (AM|PM) to (\d{1,2}:?\d{0,2}) (AM|PM)"

    match = re.search(pattern, time_frame)

    if match:
        first_time = convert_to_24_hour(match.group(1), match.group(2))
        second_time = convert_to_24_hour(match.group(3), match.group(4))
        return f"{first_time} to {second_time}"
    else:
        raise ValueError("None")

def convert_to_24_hour(time, period):
    if ":" in time:
        hours, minutes = map(int, time.split(":"))
    else:
        hours = int(time)
        minutes = 0

    if not (0 <= hours <= 12):
        raise ValueError("None")
    if not (0 <= minutes < 60):
        raise ValueError("None")

    if period == "AM":
        if hours == 12:
            hours = 0
    elif period == "PM":
        if hours != 12:
            hours +=12

    return f"{hours:02}:{minutes:02}"


if __name__ == "__main__":
    main()
