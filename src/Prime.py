def is_prime(num):
    if num < 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_in_range(start, end):
    primes = []
    for ind in range(start, end + 1):
        if is_prime(ind):
            primes.append(ind)
    return primes

# Input from the user
while True:
    try:
        number = int(input("Enter the number: "))
        break
    except ValueError:
        print("Entered value is not a valied input, expecting a whole integer number. Please enter again!")
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

choice = input(f"Do you want to find the prime numbers between the range of 0 and {number}? Press Y for 'Yes' N for 'No': ")

if choice == 'Y':
    prime_numbers = primes_in_range(0, number)
    print(f"The prime numbers between 0 and {number} are:"),
    print(prime_numbers)
else:
    print("Thank you!")
