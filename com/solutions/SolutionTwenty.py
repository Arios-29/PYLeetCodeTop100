class SolutionTwenty:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                coupled = (c == ')' and top == '(') or (c == ']' and top == '[') or (c == '}' and top == '{')
                if not coupled:
                    return False
        return len(stack) == 0
