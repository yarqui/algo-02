from collections import deque


def is_palindrome(string: str) -> bool:
    normalized_string = string.casefold().strip()
    d = deque(normalized_string)

    while len(d) > 1:
        if d.pop() != d.popleft():
            return False

    return True
