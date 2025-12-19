year = int(input("Enter the Year : "))
if 999<year<10000:
    if (year%400==0) or (year%4==0 and year%100!=0):
        print(f"Year is {year} Leap Year")
    else:
        print(f"Year is {year} Not a Leap Year")
    
else:
    print("The Year should only consists of 4 digits")
        


