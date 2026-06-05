class Solution:
    def isValid(self, s: str) -> bool:
        bigStack = []
        for c in s:
            if c in "({[":
                bigStack.append(c)
            elif bigStack and c == "]" and bigStack[-1] == "[":
                   bigStack.pop()
            elif bigStack and c == "}" and bigStack[-1] == "{":
                   bigStack.pop()
            elif bigStack and c == ")" and bigStack[-1] == "(":
                bigStack.pop()
            else:
                return False
        return True if not bigStack else False