n=int(input("Enter the number"))
harmonic=0
if n !=0:
    for i in range(1,n+1):
        harmonic+=1/i
else:
    print("Enter a valid number")       
    
print(f"The {n}th Hormonic Value is {harmonic:.3f}") 