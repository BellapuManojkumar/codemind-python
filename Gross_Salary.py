bs = int(input())
if bs<=10000:
    d = bs*0.80
    h = bs*0.20
    gs = bs+d+h
    print(f"{gs:.2f}")
elif bs<=20000:
    d = bs*0.90
    h = bs*0.25
    gs = bs+d+h
    print(f"{gs:.2f}")
elif bs>20000:
    d = bs*0.95
    h = bs*0.30
    gs = bs+d+h
    print(f"{gs:.2f}")
else:
    print(-1)