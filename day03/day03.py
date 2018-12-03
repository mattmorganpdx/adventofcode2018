from collections import defaultdict
from shared.utils import increment_dict_value


def find_spots(inputs):
    used_spots_map = defaultdict(int)
    claim_id_map = defaultdict(list)
    for _input in inputs:
        used_spots_map, claim_id_map = parse_input(_input, used_spots_map, claim_id_map)
    return sum([1 for x in used_spots_map.values() if x > 1]),\
        [claim_id for claim_id, coords in claim_id_map.items()
         if sum([1 for x in coords if used_spots_map[x] != 1]) == 0][0]


def parse_input(input_line, used_spots_map, claim_id_map):
    input_list = input_line.split(' ')
    left, top = input_list[2].rstrip(':').split(',')
    length, width = input_list[3].split('x')
    for r in range(int(left) + 1, int(left) + 1 + int(length)):
        for c in range(int(top) + 1, int(top) + 1 + int(width)):
            used_spots_map = increment_dict_value(used_spots_map, (r, c))
            claim_id_map[input_list[0]].append((r, c))
    return used_spots_map, claim_id_map
