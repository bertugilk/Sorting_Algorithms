def mergeFunction(list):
    N=len(list)
    if N>1:
        pivot=N//2
        left=list[:pivot]
        right=list[pivot:]
        mergeFunction(left)
        mergeFunction(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i = i + 1
            else:
                list[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            list[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            list[k] = right[j]
            j = j + 1
            k = k + 1

def userFunction():
    number_of_value = int(input("Enter number of value please: "))
    list = []

    for j in range(number_of_value):
        value = int(input("{0}. Value: ".format(j + 1)))
        list.append(value)
    print("Before: ", list)
    mergeFunction(list)
    print("After: ", list)

userFunction()