number=input("Enter the number : ")
status=True
for i in range(len(number)-1):
    if number[i]>number[i+1]:
        status=False
if status:
    print("YES")
else:
    print("NO")