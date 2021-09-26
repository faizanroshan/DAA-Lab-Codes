# sort the strings by their frequency and then by string comparision

def partition(strings, stringMap, start, end):

    pivot = strings[start]
    pivotIndex = start 
    low = start+1
    high = end

    while low < high:

        while (low < len(strings) and 
                    stringMap[strings[low]] <= stringMap[strings[pivotIndex]]):
                
            low += 1
        
        while (stringMap[strings[high]] > stringMap[strings[pivotIndex]]):

            high -= 1
        
        if(low < high):

            strings[low], strings[high] = strings[high], strings[low]

    strings[pivotIndex], strings[high] = strings[high], strings[pivotIndex]
    return high

def quicksort(strings, stringMap, start, end):

    if start < end:

        pi = partition(strings, stringMap, start, end)
        quicksort(strings, stringMap, start, pi-1)
        quicksort(strings, stringMap, pi+1, end)


def getFrequencyData(strings):

    stringMap = {} 
    # key = string, value = string, frequency
    for string in strings:

        if stringMap.get(string) == None:

            stringMap[string] = 1
        else:

            stringMap[string] += 1

    return stringMap 

def printStrings(stringmap):

    if (len(stringmap) < 2):

        print(stringmap[0][0])
        return 

    ptr1, ptr2 = 0, 1
    size = len(stringmap)
    while ptr1 < size and ptr2 < size:

        if stringmap[ptr1][1] != stringmap[ptr2][1]:

            print(stringmap[ptr1][1], end = " ")
        else:

            if stringmap[ptr1][0] < stringmap[ptr2][0]:

                print(stringmap[ptr1][0], end = " ")
                ptr2 = 1
                ptr1 += 1
            else:

                ptr2 = None # continue from here
        
        if ptr1 == ptr2:

            ptr2 += 1
    
    while 




if __name__ == "__main__":

    # strings = list(map(str, input().split()))
    strings = ["Roshan", "cat", "cat", "cat", "cat", "Hi", "Hi", "Hi", "Hi"]
    stringMap = getFrequencyData(strings)

    strings = list(set(strings))

    quicksort(strings, stringMap, 0, len(strings)-1)

    stringFrequencyMap = []
    for string in strings:

        stringFrequencyMap.append([strings, stringMap[string]])

    printStrings(stringFrequencyMap)
    