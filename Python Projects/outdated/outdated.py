def main():
    while True:
        input_date = input("Date: ")
        if convert_date(input_date.strip()):
             break

months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

def convert_date(input_date):
        my_order = [2, 0, 1]

        if input_date[0].isdigit():
            try:
                mid_new_date = input_date.split("/")
                month, day, year = int(mid_new_date[0]), int(mid_new_date[1]), int(mid_new_date[2])

                if month > 12 or day > 31:
                     return False

                mid_new_date = [mid_new_date[i] for i in my_order]

                print(f"{int(mid_new_date[0]):04}-{int(mid_new_date[1]):02}-{int(mid_new_date[2]):02}")
                return True
            except (ValueError, IndexError):
                 return False

        elif input_date[0].isalpha():
            try:
                if "," not in input_date:
                     return False

                alpha_list = input_date.replace(",", "").split()
                month_str, day, year = alpha_list[0], int(alpha_list[1]), int(alpha_list[2])

                if month_str in months and day <= 31:
                     month_num = months.index(month_str) + 1
                     print(f"{year:04}-{month_num:02}-{day:02}")
                     return True
                else:
                     return False
            except (ValueError, IndexError):
                 return False
        else:
            return False


main()
