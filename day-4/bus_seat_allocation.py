seats=40
n=int(input("Enter the number of requests"))

for req in range(n):
    req=int(input())
    if req<=seats:
        print("CONFIRMED")
        seats-=req
    else:
        print("WAITLISTED")
        break
    