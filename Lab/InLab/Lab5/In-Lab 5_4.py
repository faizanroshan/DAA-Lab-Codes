import sys
'''
3
2
ab
ba
2
aa
bb
'''
def longestCommonSubsequence(str1, str2):

    len1 = len(str1)
    len2 = len(str2)

    table = [[0 for x in range(0, len2+1)] for y in range(0, len1+1)]
    for char1 in range(1, len1 + 1):

        for char2 in range(1, len2 + 1):


            if str1[char1-1] == str2[char2-1]:

                table[char1][char2] = table[char1-1][char2-1] + 1
            else:

                table[char1][char2] = max(table[char1-1][char2], table[char1][char2-1])

    return table[len1][len2]

if __name__ == "__main__":

    tt = int(input())
    for _ in range(0, tt):

        numStrings = int(input())
        strings = []
        lowest = sys.maxsize
        for i in range(0, numStrings):

            string = input()
            strings.append(string)
        
        for i in range(0, len(strings)-1):

            for j in range(i+1, len(strings)):

                current = longestCommonSubsequence(strings[i], strings[j])
                lowest = min(lowest, current)
        
        print(lowest)