class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for char in tokens:
            if char == '+':
                second, first = stack.pop(), stack.pop()
                stack.append(first + second)
            elif char == '-':
                second, first = stack.pop(), stack.pop()
                stack.append(first - second)
            elif char == '*':
                second, first = stack.pop(), stack.pop()
                stack.append(first * second)
            elif char == '/':
                second, first = stack.pop(), stack.pop()
                stack.append(int(float(first) / second))
            else:
                stack.append(int(char))
        
        return stack.pop()