#!/usr/bin/env python3

def calculate(arg):
    # stack for calculator
    stack = []
    # tokenize input
    tokens = arg.split()
    # do tokens
    for token in tokens:
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            val1 = stack.pop()
            val2 = stack.pop()
            if token == '+':
                result = val1 + val2
            elif token == '-':
                result = val2 - val1
            elif token == '*':
                result = val1 * val2
            elif token == '/':
                result = val2 / val1
            stack.append(result)
            return stack[-1]

def main():
    while True:
        print(calculate(input('rpn calc> ')))

if __name__ == '__main__':
    main()
