def missing(set1,set2):
    result = []
    for item in set2:
        if item not in set1:
            result.append(item)
    return result

set1 = eval(input("Input list1: "))
set2 = eval(input("Input list2: "))
print(f"Missing values in list1 = {missing(set1, set2)}")
print(f"Additional values in list1 = {missing(set2, set1)}")
print(f"Missing values in list2 = {missing(set2, set1)}")
print(f"Additional values in list2 = {missing(set1, set2)}")

