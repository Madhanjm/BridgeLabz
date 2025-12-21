tank_capacity=1000
minute_count=0
water_fill=0
n=int(input("Enter the number of minute"))
inflow=[int(x) for x in input().split()]

for i in inflow:
    if water_fill<=tank_capacity:
        water_fill+=i
        minute_count+=1
    else:
        break
print(minute_count)