amount=int(input("Enter the amount : "))
payable_amount=0
if amount>=5000:
    payable_amount+=amount-amount*0.20
elif amount>=3000:
    payable_amount+=amount-amount*0.10
elif amount>=1000:
        payable_amount+=amount-amount*0.05
else:
    payable_amount+=amount
print(payable_amount)

    

    
