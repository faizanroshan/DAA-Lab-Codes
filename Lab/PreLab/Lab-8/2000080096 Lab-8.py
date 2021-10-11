arr = []
x = []

def echo(solutionVector):
    
    global arr
    for index in range(0, len(solutionVector)):

        if(solutionVector[index] != 0):

            print(arr[index], end = ' ')
    print('\n')

def sumOfSubset(sum, k, r):

    global arr, x, requiredSum

    # left child condition
    x[k] = 1
    if (sum + arr[k] == requiredSum):
        echo(x[:k+1])
    
    if (k < len(arr)-1 and sum + arr[k] + arr[k+1] <= requiredSum):
        sumOfSubset(sum + arr[k], k+1, r-arr[k])
    
    if(sum + r - arr[k] >= requiredSum and sum + arr[k+1] <= requiredSum):

        x[k] = 0
        sumOfSubset(sum, k+1, r-arr[k])

if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5, 6]
    x = [0 for _ in range(0, len(arr))]
    requiredSum = 8
    sumOfSubset(0, 0, sum(arr))
