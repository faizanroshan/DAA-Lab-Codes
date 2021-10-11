arr = []
flag = False
requiredSum = -1

def sumOfSubset(sum, k, r):

    global arr, requiredSum, flag

    if flag == True:
        return

    # left child condition
    if (sum + arr[k] == requiredSum):
        flag = True
    
    if (k < len(arr)-1 and sum + arr[k] + arr[k+1] <= requiredSum):
        sumOfSubset(sum + arr[k], k+1, r-arr[k])
    
    if(sum + r - arr[k] >= requiredSum and sum + arr[k+1] <= requiredSum):

        sumOfSubset(sum, k+1, r-arr[k])

def solve(arr, queries):

    global flag, requiredSum
    arraySum = sum(arr)
    for index in range(0, len(queries)):

        if arraySum < queries[index]:
            print(-1)
            continue
        else:

            requiredSum = queries[index]

            sumOfSubset(0, 0, arraySum)
            if flag == False:
                print('No')
            else:
                print('Yes')
                flag = False

if __name__ == "__main__":

    # size, q = map(int, input().split())
    # arr = list(map(int, input().split()))
    # queries = list(map(int, input().split()))
    arr = [1, 7, 4]
    queries = [10, 14, 4]

    arr.sort()
    solve(arr, queries)
