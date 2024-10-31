from datetime import date
from datetime import timedelta
import inflect
import sys
p = inflect.engine()
import re

def main():
    print(convert_to_minutes(input("Date of Birth: ")))



def convert_to_minutes(user_date):
    pattern = r"\d{4}-\d{2}-\d{1,2}"
    if match := re.search(pattern, user_date):
        new_date = date.today() - date.fromisoformat(match.group(0))
        return f"{(p.number_to_words(new_date.days * 24 * 60).replace("and ", "")).capitalize()} minutes"
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()

