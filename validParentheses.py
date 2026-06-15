class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {'}': '{', ')': '(', ']': '['}

        for c in s:
            if c in lookup.values():
                stack.append()
            elif stack and lookup[c] == stack[-1]:
                stack.pop()
            else:
                return False
            
        return stack == []


# use stack (LIFO) to append the parentheses
# have a dictionary that would classify the key-value pairs of the open/closed parentheses
# loop through string, if the character is a value in the dict, then it's an open parentheses so append to the stack
# otherwise it is a key value (closing brace), check if stack contains elements and check if the last element of the stack is the same as the value of the key
# return false otherwise
# return the status of the stack (true if it contains nothing, false if it contains elements since all open/closed parentheses should be cancelled out)