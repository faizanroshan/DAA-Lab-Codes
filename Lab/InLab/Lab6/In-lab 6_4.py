def countPossibleSubstring(string, length, substring):

    length = len(string)
    pos = [length for _ in range(0, 10)]
    dp = [0 for _ in range(0, len(string))]

    for index in range(0, len(string)):

        if string[index] in substring:
            pos[int(string[index])] = index + 1
            


    for index in range(0, len(string)):



if __name__ == "__main__":
 
    string = '453216'
    length_substring = 3
    substring = '321'

    countPossibleSubstring(string, length_substring, substring)