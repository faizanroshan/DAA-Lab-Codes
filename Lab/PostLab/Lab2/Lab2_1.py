def mergesort(arr):

    if len(arr) > 1:

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        lIndex = rIndex = index = 0

        print(left, right)
        while lIndex < len(left) and rIndex < len(right):

            if left[lIndex] <= right[rIndex]:
                
                arr[index] = left[lIndex]
                index += 1
                lIndex += 1
                
            else:

                arr[index] = right[rIndex]
                index += 1
                rIndex += 1
                
        while lIndex < len(left):

            arr[index] = left[lIndex]
            lIndex += 1
            index += 1
            
        while rIndex < len(right):

            arr[index] = right[rIndex]
            rIndex += 1
            index += 1


        
if __name__ == "__main__":


    size = int(input())
    arr = list(map(int, input().split()))
    mergesort(arr)
        