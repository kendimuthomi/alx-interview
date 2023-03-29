#!/usr/bin/python3
"""script to unlock a list of lists"""

def canUnlockAll(boxes):
    """Method that determines if all boxes can be unlocked"""
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key >= 0 and key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
