p,c,b,m,cs = map(int,input().split())
a = int((p+c+b+m+cs)/5)
if a>=90:
    print('Grade A')
elif a>=80:
    print('Grade B')
elif a>=70:
    print('Grade C')
elif a>=60:
    print('Grade D')
elif a>=40:
    print('Grade E')
else:
    print('Grade F')
