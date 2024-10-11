
#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False
    
    keys = {0}  # Start with the first box (index 0) opened
    opened_boxes = [False] * len(boxes)  # Track opened boxes
    opened_boxes[0] = True  # We can open the first box

    # Loop until no new keys can be found
    for i in range(len(boxes)):
        if opened_boxes[i]:  # If this box is opened
            for key in boxes[i]:  # Check its keys
                if key < len(boxes) and not opened_boxes[key]:
                    opened_boxes[key] = True  # Mark the box as opened
                    keys.add(key)

    return all(opened_boxes)  # Return True if all boxes are opened

