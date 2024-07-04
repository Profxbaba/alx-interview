#!/usr/bin/python3
"""
Module for checking if all lockboxes can be opened.
"""

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines if all lockboxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists where each inner list contains
                                 keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        current = queue.pop(0)
        for key in boxes[current]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)


if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))
