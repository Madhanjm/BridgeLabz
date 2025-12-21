distance=float(input("Enter the Distance"))
age=int(input("Enter the age"))
fare=distance*2
if age<12:
    #50% discount
    fare*=0.50
elif age>60:
    # 30% discount
    fare*=0.70

print(fare)
