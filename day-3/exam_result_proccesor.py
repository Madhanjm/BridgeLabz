m1,m2,m3,m4,m5=[int(x) for x in input("Enter the marks of 5 subject").split()]
if m1<35 or m2<35 or m3<35 or m4<35 or m5<35:
    print("FAIL")
elif (m1+m2+m3+m4+m5)/5 >=75:
    print("DISTINCTION")
else:
    print("PASS")    