from collections import deque


def is_palindrome(string):
    d = deque(string)

    while len(d) > 1:
        if d.pop() != d.popleft():
            return False

    return True
