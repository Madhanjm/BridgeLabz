number = int(input("Enter a number: "))
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

while number >= 10:  
    number = sum_of_digits(number)  
print(number)
