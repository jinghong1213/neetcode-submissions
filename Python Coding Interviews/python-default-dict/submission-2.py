from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    
    output = defaultdict(int)

    for count in s:
        output[count] += 1

    return output 


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    
    output = defaultdict(list)
    
    for num in nums:
        key = num[0]  #first number set to key
        value = num[1:]  #value set to save all number after 1st number
        output[key].extend(value)   #combine both of them into dict
            
    
    return output


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
