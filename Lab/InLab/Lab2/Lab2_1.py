

if __name__ == "__main__":

    size = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    check_value = 2
    index = 0
    while index < len(arr):

        if arr[index] >= check_value:

            check_value += 2
            
        index += 1
            
    print(check_value)        