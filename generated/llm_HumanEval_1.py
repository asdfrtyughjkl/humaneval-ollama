from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    groups = []
    group = ''
    
    for c in paren_string:
        if c == ' ':
            continue
        elif c == '(':
            stack.append(c)
            group += c
        elif c == ')':
            if stack:
                stack.pop()
                group += c
                if not stack:
                    groups.append(group)
                    group = ''
            else:
                group += c
                group = group.replace('(', '').replace(')', '')
                groups.append(group)
                group = ''
    
    return groups

