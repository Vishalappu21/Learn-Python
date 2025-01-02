List = list(map(int, input("Enter the Element to convert into List:").split()))
print(List)
for i in List:
    if i % 2 != 0:
        print(i)