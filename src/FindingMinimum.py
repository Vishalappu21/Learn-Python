List_2 = list(map(int, input("Enter the element to convert into List:").split()))
print(List_2)
Small = List_2[0]
for i in List_2:
    if i < Small:
        Small = i
print(f"The Smallest Number in the List is:{Small}")