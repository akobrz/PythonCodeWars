def first_non_consecutive(arr):
    if arr is not None:
        actual_element = arr[0]
        for e in arr[1:]:
            if actual_element + 1 != e:
                return e
            else:
                actual_element = e
    return None

print(first_non_consecutive([4,6,7,8,9,11]))