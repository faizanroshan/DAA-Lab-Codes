import sys

def findMinIndex(arr, index):

    returnIndex = -1
    minimum = sys.maxsize
    for i in range(index, index+4):

        if arr[i] < minimum:

            returnIndex = i 
    # print(returnIndex)
    return returnIndex

def pleaseTakeLeave(arr):

    index = 0
    leaveValue = 0
    while(index+3 < len(arr)):

        minIndex = findMinIndex(arr, index)
        leaveValue += arr[minIndex]
        index = minIndex + 1
    print(leaveValue)

if __name__ == "__main__":

    # size = int(input())
    # arr = list(map(int, input().split()))

    size = 8
    arr = [3, 2, 3, 2, 3, 5, 1, 3]
    pleaseTakeLeave(arr)