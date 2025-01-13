def isBalanced(s):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs.keys():
            if not stack or stack[-1] != bracket_pairs[char]:
                return "NO"
            stack.pop()

    if not stack:
        return "YES"
    else:
        return "NO"


n = int(input()) 
for i in range(n):
    s = input() 
    print(isBalanced(s))
