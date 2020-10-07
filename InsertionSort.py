def insertionFunction(list):
    for i in range(1, len(list)):
        insert = list[i]
        k = i
        while k > 0 and insert < list[k - 1]:
            list[k] = list[k - 1]
            k = k - 1
        list[k] = insert
def userFunction():
    number_of_value = int(input("Enter number of value please: "))
    list = []

    for j in range(number_of_value):
        value = int(input("{0}. Value: ".format(j+1)))
        list.append(value)
    print("Before: ",list)
    insertionFunction(list)
    print("After: ",list)

userFunction()