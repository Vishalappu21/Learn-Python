def is_monotonic(lst):
    return all(x <= y for x, y in zip(lst, lst[1:])) or all(x >= y for x, y in zip(lst, lst[1:]))
lst = [100,50,200,150,1000]
print(is_monotonic(lst))  