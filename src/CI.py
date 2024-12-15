def calculate_compound_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual rate of interest: "))
    time = float(input("Enter the time period (in years): "))
    compounding_frequency = int(input("Enter the number of times interest is compounded per year: "))
    
    amount = principal * (1 + rate / (100 * compounding_frequency))**(compounding_frequency * time)
    
    compound_interest = amount - principal
    
    print(f"The Compound Interest is: {compound_interest:.2f}")
    print(f"The Total Amount is: {amount:.2f}")
    
calculate_compound_interest()
