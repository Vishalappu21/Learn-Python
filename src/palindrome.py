def ispalindrome(s):
-   return s == s[::-1]
-s = "Vishal"
-A = ispalindrome(s)
-if A:
-   print("Yes")
-else:
-   print("No")


-for A in range(0,100):
-   if all(A % i !=0 for i in range(2,A)):
-     print(A, "Prime Number")