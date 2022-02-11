class ValidParentheses:
    def is_valid(self, parentheses: str) -> bool:
        if not parentheses or len(parentheses) < 2:
            return False
        stack = []
        close_to_open = {'}': '{', ')': '(', ']': '['}

        for c in parentheses:

            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) < 1
