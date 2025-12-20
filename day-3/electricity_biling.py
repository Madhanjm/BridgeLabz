units=int(input("Enter the number of units consumed"))
total_bill=0
temp_units=units

if units>200:
    total_bill=(100*3)+(100*5)+((units-200)*8)
elif  units>100:
    total_bill=(100*3)+((units-100)*5)
else:
    total_bill=units*3

if(temp_units>300):
    total_bill=total_bill*0.10
    
print(total_bill)

