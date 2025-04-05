def symmetric_brackets(string: str) -> bool:
    stack = []
    bracket_map = {"(": ")", "[": "]", "{": "}"}
    opening = set(bracket_map.keys())
    closing = set(bracket_map.values())

    for char in string:
        if char in opening:
            stack.append(bracket_map[char])
            continue

        if char in closing:
            if not stack or char != stack.pop():
                return f"{string} has asymmetric brackets"

    return (
        f"{string} has symmetric brackets"
        if not stack
        else f"{string} has asymmetric brackets"
    )
