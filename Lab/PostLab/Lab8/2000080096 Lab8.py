def allCombo(arr):

    powerset = [[]]

    for index in range(0, len(arr)):

        for insertIndex in range(0, 2**index):

            temp = [x for x in powerset[insertIndex]]
            temp.append(arr[index])
            powerset.append(temp)
            print(powerset)
            print()

    print(powerset)
if __name__ == "__main__":

    allCombo([1, 2, 3, 4])