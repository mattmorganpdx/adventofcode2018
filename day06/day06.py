from itertools import product


def day06(inputs, region_size):
    input_list = list()
    for _input in inputs:
        input_list.append(input_to_tuple(_input))
    # Get the limits for valid points
    lowest_x = sorted(input_list, key=lambda x: x[0])[0][0]
    lowest_y = sorted(input_list, key=lambda x: x[1])[0][1]
    highest_x = sorted(input_list, key=lambda x: x[0], reverse=True)[0][0]
    highest_y = sorted(input_list, key=lambda x: x[1], reverse=True)[0][1]
    # Create a list of all points in the finite grid
    valid_points = list(product(list(range(lowest_x, highest_x + 1)), list(range(lowest_y, highest_y + 1))))

    # Get the boarders for the grid for disqualifying inputs later
    top = list(product([highest_x], list(range(lowest_y, highest_y + 1))))
    bottom = list(product([lowest_x], list(range(lowest_y, highest_y + 1))))
    left = list(product(list(range(lowest_x, highest_x + 1)), [lowest_y]))
    right = list(product(list(range(lowest_x, highest_x + 1)), [highest_y]))
    # Merge the border arrays
    borders = top + bottom + left + right

    # Rule out the initial inputs based on the limits because some have obviously infinite coverage.
    valid_spots = list()
    for i in input_list:
        if lowest_x < i[0] < highest_x and lowest_y < i[1] < highest_y:
            valid_spots.append(i)

    # Create a map to hold the winning input of each point and a counter for part 2's region size
    points_map = dict()
    region_count = list()
    for p in valid_points:
        total_distance = int()
        for q in input_list:
            current_distance = mat_distance(p, q)
            total_distance += current_distance
            if points_map.get(p):
                current_winning_distance = points_map.get(p).get('dist')
                # If an input ever has a tie invalidate it
                if current_winning_distance == current_distance:
                    points_map[p]['winner'] = None
                elif current_winning_distance > current_distance:
                    points_map[p]['winner'] = q
                    points_map[p]['dist'] = current_distance
            else:
                points_map[p] = dict()
                points_map[p]['winner'] = q
                points_map[p]['dist'] = current_distance
        # if the total distance is less than the region_size arg then add it to the counter
        if total_distance < region_size:
            region_count.append(total_distance)

    # Remap the points map to a winners map
    winners_map = dict()
    for k, v in points_map.items():
        winners_map.setdefault(v.get('winner'), []).append(k)
    # Disqualify any input that won a space on the border. That means it's actually infinite
    disqual_list = list()
    for k, v in winners_map.items():
        for e in v:
            if e in borders:
                disqual_list.append(k)

    # Create a list of the area sums so we can return the larges area covered
    sums_of_areas = list()
    for q in valid_spots:
        if q not in disqual_list:
            sums_of_areas.append(sum([1 for x in points_map.values() if x.get('winner') == q]))
    return sorted(sums_of_areas)[-1], len(region_count)


def input_to_tuple(_input):
    ret = _input.split(',')
    return int(ret[0]), int(ret[1])


def mat_distance(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

