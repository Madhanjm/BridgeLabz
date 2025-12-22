number=int(input("Enter the number : "))
original_number=number
reversed_num=0
while number > 0:
    last_digit = number % 10        
    reversed_num = reversed_num * 10 + last_digit  
    number = number // 10  
if reversed_num==original_number:
    print("PALINDROME")
else:
    print("NOT A PALINDROME")