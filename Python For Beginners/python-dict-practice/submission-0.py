from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:

    my_dict = {}
    for key in word:
        if key in my_dict:
            my_dict[key] += 1
        else:
            my_dict[key] = 1

    return my_dict


# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
