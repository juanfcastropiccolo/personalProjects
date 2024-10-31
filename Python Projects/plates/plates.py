def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if two_letters_validation(plate):
        if maxmin_validation(plate):
            if middle_number_validation(plate):
                if dot_space_validation(plate):
                    return True
    return False


def two_letters_validation(plate):
    if plate[:2].isalpha():
        return True
    return False

def maxmin_validation(plate):
    if len(plate) >= 2 and len(plate) <= 6:
        return True
    return False

def middle_number_validation(plate):
    for i, char in enumerate(plate):
        if char.isdigit():
            if char == "0":
                return False
            if plate[i:].isdigit():
                return True
            else:
                return False
    return True

def dot_space_validation(plate):
    for digit in plate:
        if digit in (",", ".", "_", " "):
            return False
    return True


main()
