class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for J in s:
            if J=="(":
                stack.append(")")
            elif J=="{":
                stack.append("}")
            elif J=="[":
                stack.append("]")
            else:
                if not stack or J!=stack[-1]:
                    return False
                stack.pop()
        if stack:
            return False
        return True         