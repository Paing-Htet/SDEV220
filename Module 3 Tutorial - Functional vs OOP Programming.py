# =======================================================================================================================

def SortList(array):
    a = 0
    b = 0
    c = 0
    ReturnedList = []
    for i in array:
        if i == 0:
            a += 1

        elif i == 1: 
            b += 1

        elif i == 2: 
            c += 1

    for i in range(a+b+c):
        if a > 0:
            ReturnedList.append(0)
            a -= 1
        elif b > 0:
            ReturnedList.append(1)
            b -= 1
        elif c > 0:
            ReturnedList.append(2)
            
    return ReturnedList

# =======================================================================================================================

def binary_search(array, k):
    Lower = 0
    Upper = len(array) - 1
    Index = -1

    while Lower <= Upper:
        Middle = int((Lower + Upper) / 2)
        if array[Middle] == k:
            Index = Middle
            Upper = Middle - 1 
        elif array[Middle] < k:
            Lower = Middle + 1
        else:
            Upper = Middle - 1

    return Index

array = [3, 12, 17, 25, 38, 41, 45, 57, 63, 64, 68, 70, 74, 78, 80, 82, 86, 91, 94, 97]
k = 64

print(f"The integer {k} that you were looking for can be found at index {binary_search(array, k)}")

