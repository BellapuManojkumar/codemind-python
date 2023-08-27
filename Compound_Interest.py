p = float(input())
r = float(input())
t = float(input())
am = p*(1+r/100)**t
ci = round(am-p,2)
print(f"{ci:.2f}")
