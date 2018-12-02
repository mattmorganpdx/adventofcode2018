from collections import defaultdict
from shared.utils import increment_dict_value


def checksum(inputs):
    count_of_twos = int()
    count_of_threes = int()
    matched_boxes = list()
    for _input in inputs:
        letter_counts = defaultdict(int)
        for letter in _input:
            letter_counts = increment_dict_value(letter_counts, letter)
        if 2 in letter_counts.values():
            count_of_twos += 1
            matched_boxes.append(_input)
        if 3 in letter_counts.values():
            count_of_threes += 1
            matched_boxes.append(_input)
    return count_of_twos * count_of_threes, find_overlap(matched_boxes)


def find_overlap(matched_boxes):
    input_len = len(matched_boxes[0])
    matched_boxes = set(matched_boxes)
    for outer_box in matched_boxes:
        for inner_box in matched_boxes:
            overlap = [x for idx, x in enumerate(outer_box) if x == inner_box[idx]]
            if len(overlap) == (input_len - 1):
                return overlap
