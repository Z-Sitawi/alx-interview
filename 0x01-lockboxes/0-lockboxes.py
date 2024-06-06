#!/usr/bin/python3
""" A method that determines if all the boxes can be opened """


def canUnlockAll(boxes):
    """
        A method that determines if all the boxes can be opened
    :param boxes: a list of lists
    :return: true if all boxes can be opened, False otherwise.
    """
    nbr_boxes = len(boxes)
    keys = [0]
    counter = 0
    idx = 0

    while idx < len(keys):
        processed_key = keys[idx]
        for key in boxes[processed_key]:
            if 0 < key < nbr_boxes and key not in keys:
                keys.append(key)
                counter += 1
        idx += 1

    return counter == nbr_boxes - 1
