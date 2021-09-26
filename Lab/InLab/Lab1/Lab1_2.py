
if __name__ == "__main__":

    order = "worldabcefghijkmnpqstuvxyz"
    strings = [ "word", "world", "row"]
    
    result = sorted(strings, key= lambda string : [order.index(character) for character in string])
    print(result)