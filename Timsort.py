import random
import numpy
import math

def InsertionSort(array):# creating the Insertion algorithm
    for i in range (1,len(array)):
        for j in range(i,0,-1):
            if array[j] < array[j-1]:
                temp = array[j]# using a temp (sort for temperory) so i can move the values
                array[j] = array[j-1]
                array[j-1] = temp
            else:
                break # stops the loop so i do not waste time
            j = j - 1
    return array # returns the sorted array


def MergeArrays(arrayA, arrayB):
    counterA = 0 # initializing counter to count the elements of the list
    counterB = 0
    arrayC = [] # creating a empty list to pass the elements of both the lists
    while counterA < len(arrayA) and counterB < len(arrayB):
        if arrayA[counterA] > arrayB[counterB]:
            arrayC.append(arrayA[counterA])# passsing the value from the A list
            counterA = counterA + 1
        elif arrayA[counterA] < arrayB[counterB]:
            arrayC.append(arrayB[counterB])# passing the value from the B list
            counterB = counterB + 1
        else:
            arrayC.append(arrayB[counterB])
            arrayC.append(arrayA[counterA])
            counterA = counterA + 1
            counterB = counterB + 1
# in the rest of the section we look which list have still some elements because eventually one will
#run out of elements and the other will still have atleast one
    while counterB != len(arrayB):
        arrayC.append(arrayB[counterB])
        counterB = counterB + 1

    while counterA != len(arrayA):
        arrayC.append(arrayA[counterA])
        counterA = counterA + 1
# returning the new array which is the combination of boths
    return arrayC

def Timsort(array):
    # here we choose for how many elements only the Insertion algorithm will be used
    space = 32
    for i in range(0, len(array), space):
        array[i : i + space] = InsertionSort(array[i : i + space])

    while len(array) > space:
        for i in range(0, len(array), space * 2):
            array[i : i + space * 2] = MergeArrays(array[i : i + space], array[i + space : i + space * 2])
        space = space * 2
    #in these part i will add some code to check if the list has a -0 and +0 to make sure that they go in the correct position
    zero_sorting(array)
    #here my code will sort nans
    for i in range(0,len(array)):
        if math.isnan(array[i]):# it checks to see if there is a nan in the list
            global nan_array 
            nan_array = []
            nan_sorting(array,nan_array)
            print("A array with the name nan_array was created to store the nan's that your list had ")
            break # it breaks the loop to save time, if there is at least one nan in the list we will use the function
    print(array)

def zero_sorting(array):
    #in these part i will add some code to check if the list has a -0 and +0 to make sure that they go in the correct position
    infinity = math.inf # creating a variable with a infinity value
    for i in range(0, len(array)):
        # i chexk all the elements of the list to see if there any consecutives zeros
        if (array[i] == 0) and (array[i+1]== 0):
            #if there are 2 consecutive zeros i use the logic that 1/(a negative zero) gives negative infinity
            #and if 1/(a postitive zero) gives postitive infinity
            # so if there are 2 consecutive zeros i check if the first when it is the denominator gives postive infinity and
            #if the secodn when it is the denominator gives negative infinity
            #and if that is the case i swap the numbers
            if (numpy.float64(1.0) / array[i] == infinity) and (numpy.float64(1.0) / array[i+1] == - infinity):
                # i use numpy.float because python cannot devide a number by zero, but with the use of numpy module i can devide with z
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp

def nan_sorting(array,array_nan):
    # i have to go backwards because if i delete a element all the others move back a space so i would run in list index out of range error
    for i in range (len(array)-1, -1,-1):
        if math.isnan(array[i]):# it checks to see if there is a nan in the list
            array_nan.append(array[i])
            del array[i]# deletes the element from the list
