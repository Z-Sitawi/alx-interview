#!/usr/bin/python3
""" A method that determines if all the boxes can be opened """


def canUnlockAll(boxes):
    # Number of boxes
    nbr_boxes = len(boxes)
    # Initialize a set to store keys possessed
    keys_possessed = set(boxes[0])

    # Iterate through boxes starting from index 1
    for idx in range(1, nbr_boxes):
        # Check if the box index is in the keys possessed
        if idx in keys_possessed:
            # Add all keys in the box to keys possessed
            keys_possessed.update(boxes[idx])

    if len(keys_possessed) >= nbr_boxes - 1:
        return True
    else:
        return False
