def first_n_characters(s: str, n: int) -> str:
    return s[:n] #<<<< start from first n character from s, so start from beginning and end at n

def last_n_characters(s: str, n: int) -> str:
    return s[len(s)-n:] #<<< start from last n character from s to end, so total length of s - n


# do not modify below this line
print(first_n_characters("NeetCode", 3))
print(first_n_characters("NeetCode", 4))
print(first_n_characters("NeetCode", 8))

print(last_n_characters("NeetCode", 3))
print(last_n_characters("NeetCode", 4))
print(last_n_characters("NeetCode", 8))
