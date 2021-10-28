i=int(input("Wprowadź liczbę: "))
if i==0:
    print("0")
elif i==1:
    print("1")
else:
    f1=0
    f2=1
    for a in range(i-1):
        f1,f2=f2,f1+f2
    print(f2)