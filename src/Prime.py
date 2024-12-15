def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Input from the user
num = int(input("Enter the number: "))

if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

choice = input( "Press Y for 'Yes' N for 'No': ")

if choice == 'Y':
    prime_numbers = primes_in_range(0, 200)
    print("The prime numbers between 0 and 70 are:")
    print(prime_numbers)
else:
    print("Thank you!")
