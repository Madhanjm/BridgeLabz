salary=int(input("Enter the salary : "))
late_days=int(input("Enter the late days : "))
absent_days=int(input("Enter the absent days : "))
if late_days>10:
    salary-=salary*0.10
elif late_days>5:
    salary-=salary*0.05
if(absent_days>2):
    salary-=salary*0.05
print(salary)