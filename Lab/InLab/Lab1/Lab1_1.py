def sortStrings(vector):

    for i in range(0, len(vector)):

        for j in range(i+1, len(vector)):

            if vector[i][0] > vector[j][0]:
                
                temp = vector[i]
                vector[i] = vector[j]
                vector[j] = temp
            
            elif vector[i][0] == vector[j][0]:

                if vector[i][1] > vector[j][1]:
                    
                    temp = vector[i]
                    vector[i] = vector[j]
                    vector[j] = temp

    for index in range(0, len(vector)):

        print(vector[index][1], end = " ")


if __name__ == "__main__":

    #strings = list(map(str, input().split()))
    strings = ["Ramesh", "Mahesh", "Ramesh", "Mahesh"]
    stringMap = {}
    for string in strings:

        stringMap[string] = stringMap.get(string, 0) + 1

    vector = [[stringMap[key], key] for key in stringMap]
    sortStrings(vector)
    


        