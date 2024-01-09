def is_prime(number):
    if number < 2:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True


for b in range(1, 101):
    if is_prime(b):
        print(b , end=" ")