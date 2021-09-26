

def getVowelCount(string):

    vowel = {"a" : True, "e": "True", "i":True, "o":True, "u":True}
    count = 0
    for ch in string:

        if vowel.get(ch) != None:

            count += 1
    
    return count
if __name__ == "__main__":

    #strings = list(map(str, input().split()))
    strings = ["pointer", "for", "array", "code"]
    vector = []
    for string in strings:

        vector.append([getVowelCount(string), string])
    
    vector.sort()
    print(vector)