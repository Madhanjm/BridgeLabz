import random

while True:
    flip=int(input("Enter number of times to flip the coin : "))
    if flip>0:
        break
    else:
        print("Enter the positive Number")

head=0
tail=0
for i in range(flip):
    random_flip=random.random()
    if random_flip <0.5 :
        tail+=1
    else :
        head+=1

print(f"Percentage of Head {(head/flip)*100} %")
print(f"Percentage of Tail {(tail/flip)*100} %")    
