L_2 = list(map(int, input("Enter the element to convert into list:").split()))
print(L_2)
remove = [12, 45, 60]
res = []
for i in L_2:
    if i not in remove:
        res.append(i)
print(res)
