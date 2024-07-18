def is_correct(s):
    stack = []
    opening = "({[<"
    closing = ")}]>"
    matches = {')': '(', '}': '{', ']': '[', '>': '<'}
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != matches[char]:
                return False
            stack.pop()

    return not stack
import re
s = ''
result = ''
try:
    with open('input.txt', 'r') as f:
        s = f.read()
except FileNotFoundError:
    print(f"Error: The file does not exist.")
lines = s.split('\n')
for line in lines:
    line = re.sub(r'[^()\[\]{}<>]', '', line)
    result = result +  str(is_correct(line)) + '\n'
try:
    with open('output.txt', 'w') as f:
        f.write(result)
except IOError:
    print("Error: Unable to write to output.txt")
