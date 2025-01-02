List = list(map(int, input("Enter the element to Convert into List:").split()))
print(List)
for i in List:
    if i % 2 == 0:
        print(f"the Even number in the List are {i}")