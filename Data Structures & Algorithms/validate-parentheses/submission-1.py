class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', '}': '{', ']': '['}
    
        for char in s:
            if char not in hashmap:
            # If it's an opening bracket, add to stack
                stack.append(char)
            else:
            # If it's a closing bracket, check for a match
                if not stack or stack.pop() != hashmap[char]:
                    return False
    
        return not stack