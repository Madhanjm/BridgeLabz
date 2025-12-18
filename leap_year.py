year = input("Enter the Year : ")
while True:
    if len(year) ==4 :
        break
    else:
        print("The Year should only consists of 4 digits")

year=int(year)
if (year%400==0) or (year%4==0 and year%100!=0):
    print(f"Year is {year} Leap Year")
else:
    print(f"Year is {year} Not a Leap Year")