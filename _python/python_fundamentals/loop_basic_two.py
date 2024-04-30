
#1
def biggie_size(array): 
    for i in range(len(array)):
        if array[i]>0:
            array[i]='big'
    return array
print(biggie_size([0,10,-5,9,9,6,3,2]))

#2
my_list = [1,2,8,5,6,90]
def count_positives(array):
    count = 0
    for i in array:
        if i > 0:
            count += 1

    array[-1] = count
    return array

print(count_positives(my_list))

#3
myList = [5,8,9,-7]
def sum_total(array):

    sum_myList = 0
    for i in myList:

        sum_myList = sum_myList + i

    return sum_myList

print(sum_total(array=myList))

#4

def Average(list):
    sum = 0
    for i in list:
        sum += i
    return (sum/len(list))
print(Average([1,2,3,4,5,6,7]))

#5

def length(list):
    return len(list)
print(length([15,2,1,-9,8]))
print(length([]))

#6

def min(list):
    if len(list)<0:
        return False
    minInt = list[0]
    for i in list:
        if i<minInt:
            minInt = i
    return minInt
print(min([37,2,1,-15]))

#7

def max(list):
    if len(list)<0:
        return False
    maxInt = list[0]
    for i in list:
        if i>maxInt:
            maxInt = i
    return maxInt
print(max([37,2,1,-15]))

#8

def Ultimate_Analysis(list):

    dictionary = {}
    dictionary["sumTotal"] = sum_total(list)
    dictionary["average"] = Average(list)
    dictionary["minimum"] = min(list)
    dictionary["maximum"] = max(list)
    dictionary["length "] = length(list)
    return dictionary

print(Ultimate_Analysis([37,2,1,-9]))

#9

def Reverse_List(list):
    for i in range(0, (len(list)-1)):
        reverse = list[i]
        list[i] = list[len(list)-1-i]
        list[len(list)-1-i] = reverse
    return list
print(Reverse_List([38,2,4,-7]))