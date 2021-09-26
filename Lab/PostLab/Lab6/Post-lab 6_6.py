def solve(n, k, string):

    arr = [1]
    for i in range(len(string)):

        total = 0
        j = i

        while(j >= 0):

            if(int(string[j:i + 1]) < k):

                total = (total + arr[j]) % (10**9 + 7)
            else:
                break
            j -= 1

        arr.append(total)
        
    return arr[-1] % (10**9 + 7)
    
if __name__ == "__main__":

    n, k = map(int, input().split())
    string = input()
    print(solve(n, k, string))