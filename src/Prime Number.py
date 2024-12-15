for A in range(0,100):
   if all(A % i !=0 for i in range(2,A)):
     print(A, "Prime Number")