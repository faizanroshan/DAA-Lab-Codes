
if __name__ == "__main__":

    # tt = int(input())
    tt = 1
    for _ in range(0, tt):

        # size = int(input())
        # arr = list(map(int, input().split()))
        size = 5
        arr = [9, 8, 1, 8, 4]

        frequency = {}
        for index in range(0, size):

            if frequency.get(arr[index]) == None:

                frequency[arr[index]] = 1
            else:
                frequency[arr[index]] += 1

        maximumFrequency = 0
        for index in range(0, len(arr)):

            if frequency[arr[index]] > maximumFrequency:

                maximumFrequency = frequency[arr[index]]
        
        print(len(arr) - maximumFrequency)
