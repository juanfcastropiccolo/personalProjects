import validators


user_input = input("What's your email address? ")

if validators.email(user_input):
    print("Valid")
else:
    print("Invalid")



