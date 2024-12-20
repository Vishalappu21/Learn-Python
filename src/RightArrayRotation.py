arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
a = 1
Right_rotation = arr[-a:] + arr[:-a]
print(f"the leftRotation of an array is {Right_rotation}")