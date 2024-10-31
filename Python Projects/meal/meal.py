def main():

    time_input = input("What time is it? ").strip()
    time_in_hours = convert(time_input)

    if 7.0 <= time_in_hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_in_hours <= 13.0:
        print("lunch time")
    elif 18.0 <= time_in_hours <= 19.0:
        print("dinner time")
    else:
        print()

def convert(time_input):

    if "a.m." in time_input or "p.m." in time_input:
        time_input = time_input.replace("a.m.", "").replace("p.m.","").strip()
        hours, minutes = map(int, time_input.split(":"))

        if "p.m." in time_input and hours != 12:
            hours += 12
        if "a.m." in time_input and hours == 12:
            hours = 0
        return hours + minutes / 60

    else:
        hours, minutes = map(int, time_input.split(":"))
        return hours + minutes / 60



if __name__ == "__main__":
    main()
