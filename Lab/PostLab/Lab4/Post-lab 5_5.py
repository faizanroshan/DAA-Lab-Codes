
if __name__ == "__main__":

    # arr = list(map(int, input().split()))
    arr = [3, 3, 3, 3, 3, 1, 3]
    length = len(arr)

    # for making a map of group size 
    groupIndexPair = {}

    for index in range(0, len(arr)):

        if groupIndexPair.get(arr[index]) == None:

            groupIndexPair[arr[index]] = []

        groupIndexPair[arr[index]].append(index)
    

    output = []
    for groupSize in groupIndexPair.keys():

        limit = 0
        length = len(groupIndexPair[groupSize])
        group = groupIndexPair[groupSize]
        temp = []
        for index in range(0, length):

            if limit == groupSize: # for printing each group at a time
                output.append(temp)
                temp = []
                limit = 0

            temp.append(group[index])
            limit += 1
        output.append(temp)

    print(output)