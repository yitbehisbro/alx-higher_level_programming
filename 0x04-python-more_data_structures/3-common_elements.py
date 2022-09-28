#!/us/bin/python3
def common_elements(set_1, set_2):
    intersection = []
    if set_1 is not None and set_2 is not None:
        intersection = set_1 & set_2
        return intersection
