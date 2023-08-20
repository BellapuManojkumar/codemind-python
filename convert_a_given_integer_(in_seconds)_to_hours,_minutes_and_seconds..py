i = int(input())
H = i//3600
M = (i%3600)//60
S = (i%3600)%60
print(f"H:M:S-{H}:{M}:{S}")