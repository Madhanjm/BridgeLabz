T=int(input("Enter the time in sec"))%90
if 1<=T<=30:
    print("RED")
elif 31<=T<=45:
    print("YELLOW")
elif 46<=T<=90 or T==0:
    print("GREEN")