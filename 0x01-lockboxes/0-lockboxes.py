"""
Given n number of locked boxes, where each box is numbered sequentialy
from 0 to n-1 and each box containing keys to the other boxes, the
following function determines if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """ function to determine if all boxes can be opend
        Args:
            boxes(List): list of boxes
        Returns:
            True if all boxes can be opend and false if not
    """

    num_boxes = len(boxes)
    checked = [False] * num_boxes
    checked[0] = True
    waiting = [0]

    while waiting:
        current_box = waiting.pop(0)
        keys = boxes[current_box]

        for key in keys:
            if 0 <= key < num_boxes and not checked[key]:
                checked[key] = True
                waiting.append(key)

    return all(checked)
