List_1 = list(map(int, input("Enter the element to convert into List:").split()))
rest = 1
for i in List_1:
    rest = rest * i
print(List_1)
print(f"The element after Multiplying in the List_1 is :{rest}")