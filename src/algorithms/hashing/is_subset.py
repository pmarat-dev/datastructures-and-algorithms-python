def is_subset(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    hashset = set()

    for i in range(0, m):
        hashset.add(arr1[i])

    for i in range(0, n):
        if arr2[i] in hashset:
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]

    if is_subset(arr1, arr2):
        print("arr2[] is subset of arr1[] ")
    else:
        print("arr2[] is not a subset of arr1[] ")
