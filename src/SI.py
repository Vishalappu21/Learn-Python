def Calculte_Simple_Interest():
    principal=float(input("enter the principal amount:"))
    rate = float(input("enter the rate of interest:"))
    time = float(input("enter the time period:"))
    
    SI =(principal*rate*time)/100

    print("the simple_interest is:",SI)
    print("the Total_amount is:",(principal+SI))
    
Calculte_Simple_Interest()
    
    