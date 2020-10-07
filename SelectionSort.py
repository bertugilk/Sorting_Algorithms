def selectionFunction(list):
    N=len(list)
    for i in range(0,N-1):
        min=list[N-1]
        index=N-1
        for j in range(i,N-1):
            if list[j]<min:
                min=list[j]
                index=j
        list[index]=list[i]
        list[i]=min
def userFunction():
    number_of_value = int(input("Enter number of value please: "))
    list = []

    for j in range(number_of_value):
        value = int(input("{0}. Value: ".format(j + 1)))
        list.append(value)
    print("Before: ", list)
    selectionFunction(list)
    print("After: ", list)

userFunction()