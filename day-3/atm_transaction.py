initial_balance=float(input("Enter the intial balance: "))
n=int(input("Enter number of time you want to withdrawal:"))
"""
withdraw_amount=[]
for i in range(n):
    withdraw_amount.append(int(input()))
    """
withdraw_amount=[(int(input())) for i in range(n)]
for i in withdraw_amount:
    if i%100==0 and i <= initial_balance:
        print("SUCESS")
        initial_balance-=i
    else:
        print("FAILED")   
  
print(initial_balance) 
    
