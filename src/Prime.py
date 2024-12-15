num_int = int(input("Enter_the_number: "))
if num_int == 1:
    print("is not a prime_number")
if num_int>1:
    for n in range(2,num_int):
        if num_int%2 == 0:
            print(num_int,"is not a prime_number")
            break
        else:
            print(num_int,"is a prime_number")
        