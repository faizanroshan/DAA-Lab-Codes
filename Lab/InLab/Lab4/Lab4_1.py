if __name__ == "__main__":

    length, people = 3, 2
    cost = [2, 5, 6]
    cost.sort(reverse = True)

    finalCost = 0
    for current in range(0, people):

        increment = 1
        for index in range(current, len(cost), people):

            finalCost += (cost[index] * increment)
            increment += 1
            
    print(finalCost)



