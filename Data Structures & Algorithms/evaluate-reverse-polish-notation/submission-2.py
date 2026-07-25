class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        token_stack = []
        def isNumber(s: str) -> bool:
            try:
                int(s)
                return True
            except ValueError:
                return False
        # assume all the tokens are valid
        for token in tokens:
            if isNumber(token):
                token_stack.append(int(token))
            else:
                num1 = token_stack.pop()
                num2 = token_stack.pop()
                if token == '+':
                    token_stack.append(num2 + num1)
                elif token == '-':
                    token_stack.append(num2 - num1)
                elif token == '*':
                    token_stack.append(num2 * num1)
                elif token == '/':
                    token_stack.append(int(num2 / num1))
        return int(token_stack[-1])
        

               

        