class Solution:
    def isValid(self, s: str) -> bool:
        # () {} []
        # if ( { [, push to stack
        # else check the peak, if match pop out, if not match return False
        
        # Fail fast
        if len(s) % 2 != 0:
            return False
        
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    return False
                if(c == ')' and stack[-1] == '(') or (c == ']' and stack[-1] == '[') or (c == '}' and stack[-1] == '{'):
                    stack.pop()
                    continue
                else :
                    return False
        return len(stack) == 0