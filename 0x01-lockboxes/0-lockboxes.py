#!/usr/bin/python3
""" A method that determines if all the boxes can be opened """


def canUnlockAll(boxes):
    """
        A method that determines if all the boxes can be opened
    :param boxes: a list of lists
    :return: true if all boxes can be opened, False otherwise.
    """
    if isinstance(boxes, list):
        for box in boxes:
            if len(box) == 0 and boxes[-1] != box:
                return False
        return True
