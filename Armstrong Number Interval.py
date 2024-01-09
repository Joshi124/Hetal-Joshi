def arm(num):
    a = len(str(num))
    b = num
    sum = 0
    
    while b > 0:
        digit = b % 10
        sum += digit ** a
        b //= 10
    
    return num == sum

c = int(input("Enter a number:"))

for x in range(1,c):
    if arm(x):
        print(x, end=" ")