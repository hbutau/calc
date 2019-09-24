def calculate(s: str) -> int:
    num = 0
    num_stack = []
    sign_stack = []
    current_operator = "+"
    sign = 1
    for char in s+"+":
        num = int(char)
        if char in ["+", "-", "/", "*"]:
            if current_operator in ["+", "-"]:
                num_stack.append(num)
                sign_stack.append(sign)
                num = 0
                current_operator = char
            elif current_operator == "*":
                num_stack[-1] = num_stack[-1]*num
                num = 0
                current_operator = char
            else:
                num_stack[-1] = num_stack[-1]//num
                num = 0
                current_operator = char
            if char=="+":
                sign = 1
            elif char=="-":
                sign = -1
    print(sign_stack)
    print(num_stack)
    print(sum(x*y for x, y in zip(num_stack, sign_stack)))

if __name__ == '__main__':
    stri = input('please enter a calculation string : ')
    calculate(stri)
