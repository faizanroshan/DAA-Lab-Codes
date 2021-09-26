'''
5 3 
5 4 8 6 9 
2 3 5

'''
import sys

def getMaxArray(arr):

    minu = -sys.maxsize
    maxArr = [minu for _ in range(0, len(arr))]

    for index in range(0, len(arr)):

        maxArr[index] = max(arr[index], maxArr[index-1]) 
    return maxArr 

if __name__ == "__main__":

    size, queries = map(int, input().split())
    arr = list(map(int, input().split()))

    maxArray = getMaxArray(arr)

    queries = list(map(int, input().split()))
    for query in queries:

        print(maxArray[query - 1])