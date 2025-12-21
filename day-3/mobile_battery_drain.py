drain_per_min=int(input("Enter the Battery drain per minute"))
minutes=0
battery=100
while battery>0:
    battery=battery-drain_per_min
    minutes+=1
print(minutes)