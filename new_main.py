def check(x):
    if x.isdigit()==False:
        return False
    x=int(x)
    return x%2==0

print(f"{10256}is even? {check(10256)}")