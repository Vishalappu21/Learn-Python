num_int = int(input("Enter the number: "))

if num_int == 1:
    print(f"{num_int} is not a prime number.")
    print("Thank you")
elif num_int > 1:
    for n in range(2, num_int):
        if num_int % n == 0:
            print(f"{num_int} is not a prime number.")
            break
    else:
        print(f"{num_int} is a prime number.")

    
    print(f"Prime numbers between 0 and {num_int}:")
    for i in range(2, num_int + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, end=" ")

if num_int > 1 and not all(num_int % n != 0 for n in range(2, num_int)):
    print("\nThank you")
