def Silnia(n):
    if n == 0:
        return("None")
    if n < 2:
        return 1
    iloczyn=1
    for i in range(2,n+1):
        iloczyn *= i
    return iloczyn
x=(int(input("Podaj wartość dla której obilczyć silnię: ")))+1
for n in range(1,x):
    print(n,Silnia(n))słaba]