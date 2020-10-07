# Print Fibonacci sequence.
a, b = 1, 1
print(a, b, end=' ')
for _ in range(18):
    a, b = b, a + b
    print(b, end=' ')
print()
# Print prime.
for num in range(2, 100):
    is_prime = True
    for factor in range(2, num):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
