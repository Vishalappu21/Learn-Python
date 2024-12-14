# basic-python-question
Palindrome:-
def ispalindrome(s):
   return s == s[::-1]
s = "Vishal"
A = ispalindrome(s)
if A:
   print("Yes")
else:
   print("No")
prime Number:-
for A in range(0,100):
   if all(A % i !=0 for i in range(2,A)):
     print(A, "Prime Number")
Fibonacci Sequence:-
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
feb(100)
