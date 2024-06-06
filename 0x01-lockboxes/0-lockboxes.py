#!/usr/bin/python3
""" A method that determines if all the boxes can be opened """


def canUnlockAll(boxes):
    """
        A method that determines if all the boxes can be opened
    :param boxes: a list of lists
    :return: true if all boxes can be opened, False otherwise.
    """
    keys = set()
    keys.add(0)
    locked_boxes = [0]
    while locked_boxes:
        box_to_open = locked_boxes.pop()
        for key in boxes[box_to_open]:
            if key not in keys:
                keys.add(key)
                locked_boxes.append(key)
    return len(keys) == len(boxes)
