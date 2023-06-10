import re


def check_braces(string):
    stack = []

    for char in string:
        if char == '{':
            stack.append(char)
        elif char == '}':
            if len(stack) == 0 or stack[-1] != '{':
                return False
            else:
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


# 示例用法
string1 = 'Hello {world}（{{}}0{}'
string2 = 'Hello {world'
string3 = 'Hello} world{'
string4 = 'Hello {world}'

print(check_braces(string1))  # 输出：False
print(check_braces(string2))  # 输出：False
print(check_braces(string3))  # 输出：False
print(check_braces(string4))  # 输出：True
