def findMinimumFare(destinations, carFare, busFare):
    
    destination = [ [abs(carFare[i] - busFare[i]), i] for i in range(0, len(carFare)) ]
    destination.sort()

    index = destination[-1][1] # highestDiffereneceIndex
    selectVehicle = -1 # bus - 1 | car - 0
    if busFare[index] < carFare[index]:

        selectVehicle = 1
    else:

        selectVehicle = 0
        
if __name__ == "__main__":

    # destination = int(input())
    # carFare = list(map(int, input().split()))
    # busFare = list(map(int, input().split()))
    destination = 5 
    carFare = [3, 2, 5, 7, 19]
    busFare = [10, 1, 4, 2, 21]

    findMinimumFare(destination, carFare, busFare)
