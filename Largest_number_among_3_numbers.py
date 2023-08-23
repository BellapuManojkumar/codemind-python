x,y,z = map(int,input().split())
if x<y and z<y:
    print(y)
elif x<z and y<z:
    print(z)
else:
    print(x)
    