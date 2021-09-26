count = 0
def recursive_count(arr, low, high, k):

    global count
    if len(arr) == 1:

        if arr[0] == k:

            count += 1

        return

    else:
        mid =  len(arr) // 2 
        left = arr[:mid]
        right = arr[mid:]
        recursive_count(left, low, mid, k)
        recursive_count(right, mid, high, k)
        return

if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5, 4, 4, 5, 2, 4]
    recursive_count(arr, 0, len(arr)-1, 4)
    
    print(count)