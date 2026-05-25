def remove_fourth_character(word: str) -> str:
    before_fourth = word[:3]
    after_fourth = word[4:]
    new_word = before_fourth + after_fourth
    return new_word


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
