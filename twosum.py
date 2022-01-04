arr1 = [1,3,5,6]
target1 = 4

arr2 = [4,7,2,6]
target2 = 128

def twosum(arr, target):
    values = dict()

    for i, elem in enumerate(arr):
        comp = target-elem
        if comp in values:
            return [values[comp], i]
        values[elem] = i

    return []

list1= twosum(arr1, target1);
print(list1)

list2= twosum(arr2, target2);
print(list2)