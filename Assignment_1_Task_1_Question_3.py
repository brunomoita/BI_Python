import re

phonenumber= "brunosimoes@gmail.com"

regex= "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

if re.search(regex, phonenumber):
    print("Valid email address")
else:
    print("Invalid email address")