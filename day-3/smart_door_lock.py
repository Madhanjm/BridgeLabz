correct_pin=input("Set the pin : ")
status=False
for _ in range(3):
    attempt=input()
    if attempt==correct_pin:
        status=True
        break
if status:
    print("ACCESS GRANTED")
else:
    print("LOCKED")      