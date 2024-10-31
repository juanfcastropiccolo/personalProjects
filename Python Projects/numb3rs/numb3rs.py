import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip_address):
    if matches := re.fullmatch(r"([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip_address):
        groups = matches.groups()
        for group in groups:
            if int(group) > 255 or int(group) < 0:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
