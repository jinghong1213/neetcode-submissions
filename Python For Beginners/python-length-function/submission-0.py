def get_longer_word(word1: str, word2: str) -> str:
    str1 = len(word1)
    str2 = len(word2)
    if str1 > str2:
        return word1
    elif str2 > str1:
        return word2
    else:
        return word1
    pass



# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
