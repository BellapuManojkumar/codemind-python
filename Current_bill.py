u = int(input())
if u<199:
    n=u*1.20
elif u==200 or u<400:
    n=u*1.50
elif u==400 or u<600:
    n=u*1.80
elif u>600:
    n=u*2.00
if n>400:
    t=n*0.15
    c=t+n
    print(f"{c:.2f}")
else:
    c=n+100
    print(f"{c:.2f}")