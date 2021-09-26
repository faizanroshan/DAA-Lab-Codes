def findEven(string):

    table = [0 for _ in range(0, len(string))]
    count = 0
    for index in range(0, len(string)):

        if int(string[index]) % 2 == 0:

            count += 1

    currentValue = count
    for index in range(0, len(string)):

        if int(string[index]) % 2 == 0:
            table[index] = currentValue
            currentValue -= 1
        else:

            table[index] = currentValue
    print(table)

if __name__ == "__main__":

    findEven("475854637834259")