if __name__ == "__main__":

    # arr = list(map(int,input().split()))
    arr = [7, 6, 4, 3, 1]
    max_profit = 0
    price = arr[0]
    n = len(arr)

    for i in range(n):
        for j in range(i+1,n):
            if(arr[i] < arr[j]):
                x = arr[j]-arr[i]
                if(max_profit < x):
                    max_profit = x
                    
    print(max_profit)
