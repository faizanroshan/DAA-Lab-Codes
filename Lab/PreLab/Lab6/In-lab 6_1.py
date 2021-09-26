'''
2
2 0
2 2
'''
import math
if __name__ == "__main__":

    mod = math.pow(10, 9) + 7
    c = [[0 for x in range(0, 1001)] for y in range(0, 1001)]

    for n in range(0, 1001):

        c[n][0] = c[n][n] = 1
        for k in range(0, n):

            c[n][k] = c[n-1][k-1] + c[n-1][k]

    tt = int(input())
    for _ in range(tt):

        n, p = map(int, input().split())
        result = 0
        for i in range(0, p+1):

            result = (result % mod + c[n][i] % mod) % mod
        
        print(int(result))