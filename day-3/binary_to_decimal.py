binary_number=input("Enter the binary number : ")
pow=len(binary_number)-1
decimal_number=0
for i in binary_number:
    if i=="1":
        decimal_number+=2**pow
    pow-=1
print(decimal_number)