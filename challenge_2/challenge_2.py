d = dict()

n = 1
while n < 100:
    n += 1
    if n%3 == 0 or n%5 ==0:
        d[n] = n**2 

print(d)


for key, value in d.items():
    print(f"Key: {key} Value: {value}")