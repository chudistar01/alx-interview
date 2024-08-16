#!/usr/bin/python3
'''  Checks for opened locked boxes '''


def canUnlockAll(boxes):
    '''
    Checks for opened locked boxes
    '''
    n = len(boxes)
    seen_boxes = {0}
    unseen_boxes = set(boxes[0])

    while unseen_boxes:
        boxIdx = unseen_boxes.pop()
        if 0 <= boxIdx < n and boxIdx not in seen_boxes:
            seen_boxes.add(boxIdx)
            unseen_boxes.update(boxes[boxIdx])

    return len(seen_boxes) == n
