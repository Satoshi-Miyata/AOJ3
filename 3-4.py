a,b,c = map(int,input().split())
i = a
x = 0
while i <= b:
    if c%i == 0:
        x += 1
    i += 1
print(x)