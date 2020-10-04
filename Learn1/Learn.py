num = int(input('Please input a N*:'))
end = int(num ** 0.5)
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print(f'{num} is prime.')
else:
    print(f'{num} is not prime.')
