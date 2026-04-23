def cal(x):
    if x<=0:
        return 0
    elif x==1:
        return 1
    elif x==2:
        return 2
    for _ in range(3,x+1):
        return cal(x-1)+cal(x-2)

print(f"{5}th fibonacci number is {cal(5)}")