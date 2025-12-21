a=int(input("Enter the First Number : "))
b=int(input("Enter the second number : "))
prime_counter=0

for i in range(a,b+1):#b should be inclusive
    if i<2:
        continue
    
    is_prime=True
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            is_prime=False
    if is_prime==True:
        prime_counter+=1
print(prime_counter)