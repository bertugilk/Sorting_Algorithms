def bubbleFunction(list):
    N=len(list)
    for i in range(0,N-1):
        for j in  range(0,N-1-i):
            if list[j]>list[j+1]:
                i=list[j]
                list[j]=list[j+1]
                list[j + 1]=i

def userFunction():
    number_of_value = int(input("Enter number of value please: "))
    list = []

    for j in range(number_of_value):
        value = int(input("{0}. Value: ".format(j+1)))
        list.append(value)
    print("Before: ",list)
    bubbleFunction(list)
    print("After: ",list)

userFunction()