
def partition(values_, pivot):
    left = []
    middle = []
    right = []
    for v in values_:
        if v < pivot:
            left.append(v)
        elif v == pivot:
            middle.append(v)
        elif v > pivot:
            right.append(v)
    return left, middle, right


def quick_sort(values_):
    if not values_:
        return []
    if len(values_) == 1:
        return values_
    pivot = values_[-1]
    left, middle, right = partition(values_, pivot)
    return quick_sort(left) + middle + quick_sort(right)


assert quick_sort([])  == []
assert quick_sort([1]) == [1]
assert quick_sort([1,2]) == [1,2]
assert quick_sort([2,1]) == [1,2]
assert quick_sort([3,2,1]) == [1,2,3]
assert quick_sort([1,2,3]) == [1,2,3]
assert quick_sort([9,8,7,6,5,4,3,2,1,4]) == [1,2,3,4,4,5,6,7,8,9]
