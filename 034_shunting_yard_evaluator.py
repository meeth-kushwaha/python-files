"""Program 034: Shunting-Yard Infix to RPN Parser and Evaluator."""
import operator

OPS = {
    '+': (1, operator.add),
    '-': (1, operator.sub),
    '*': (2, operator.mul),
    '/': (2, operator.truediv)
}

def infix_to_rpn(expr: str) -> list[str]:
    tokens = expr.replace("(", " ( ").replace(")", " ) ").split()
    output, stack = [], []
    for token in tokens:
        if token.replace(".", "", 1).isdigit():
            output.append(token)
        elif token in OPS:
            while stack and stack[-1] in OPS and OPS[stack[-1]][0] >= OPS[token][0]:
                output.append(stack.pop())
            stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
    while stack:
        output.append(stack.pop())
    return output

def evaluate_rpn(tokens: list[str]) -> float:
    stack = []
    for t in tokens:
        if t in OPS:
            b, a = stack.pop(), stack.pop()
            stack.append(OPS[t][1](a, b))
        else:
            stack.append(float(t))
    return stack[0]

if __name__ == "__main__":
    print("--- 034: Shunting Yard Parser ---")
    expression = "3 + 4 * ( 2 - 1 ) / 2"
    rpn = infix_to_rpn(expression)
    res = evaluate_rpn(rpn)
    print(f"Expr: {expression}")
    print(f"RPN:  {' '.join(rpn)}")
    print(f"Result: {res}")
