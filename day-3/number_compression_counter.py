number=int(input("Enter the number"))
count=0
while number%2==0:
    count+=1
    number/=2
print(count)    