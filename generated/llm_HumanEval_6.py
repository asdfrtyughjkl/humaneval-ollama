from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    for group in paren_string.split():
        stack = 0
        nesting_level = 0
        for char in group:
            if char == '(':
                stack += 1
                nesting_level = max(nesting_level, stack)
            elif char == ')':
                stack -= 1
        result.append(nesting_level)
    return result

