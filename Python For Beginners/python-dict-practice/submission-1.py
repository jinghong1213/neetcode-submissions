from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:

    my_dict = {}
    for char in word:
        if char in my_dict:
            my_dict[char] += 1  #means value = value + 1
        else:
            my_dict[char] = 1

    return my_dict


# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
