
def load_input(filename):
    lines = list()
    with open(filename, "r") as f:
        for line in f.readlines():
            lines.append(line.strip())
    return lines


def increment_dict_value(frequency_counts, frequency):
    frequency_counts[frequency] = frequency_counts[frequency] + 1
    return frequency_counts
