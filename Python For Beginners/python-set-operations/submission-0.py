from typing import List

def count_unique_words(words: List[str]) -> int:
    my_set = set(words)
    if my_set:
        return len(my_set)
    return 0

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
