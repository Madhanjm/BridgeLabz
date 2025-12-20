password=input("Enter a password :")
is_digits=False
is_upper=False
for i in password:
    if i.isdigit():
        is_digits=True
    if i.isupper():
        is_upper=True
if len(password)>=8 and is_digits and is_upper:
    print("STRONG")
else:
    print("WEAK")
