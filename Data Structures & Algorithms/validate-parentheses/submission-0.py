class Solution:
    def isValid(self, s: str) -> bool:
        
        # use dictionary, pattern is when close(key) match open(value), remove
        stack = []
        closeToOpen = {
            ")":"(", 
            "}":"{", 
            "]":"["
        }

        for c in s:
            if c in closeToOpen:  
                if stack and stack[-1] == closeToOpen[c]:   # means array cannot be empty and match with dict's value
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
            