number=int(input("Enter the number : "))
temp=number
arm_strong=0
while temp>0:
    last_digit=temp%10
    arm_strong+=last_digit**len(str(number))
    temp//=10
if arm_strong==number:
    print("YES")
else:
    print("No")
