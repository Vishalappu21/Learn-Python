def feb(M):
   a = 0
   b = 1
   print(a)
   print(b)

   for i in range(0,M):
    c = a+b
    a = b
    b = c
    print(c)
feb(10)
