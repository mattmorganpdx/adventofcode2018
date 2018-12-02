from collections import defaultdict
from shared.utils import increment_dict_value


def calibrate(inputs, frequency=0):
    frequency_counts = defaultdict(int)
    first_repeat = None
    first_total = None
    frequency_counts[frequency] = 1
    while first_repeat is None:
        for _input in inputs:
            frequency = frequency + eval(_input)
            frequency_counts = increment_dict_value(frequency_counts, frequency)
            if frequency_counts[frequency] > 1 and first_repeat is None:
                first_repeat = frequency
        if first_total is None:
            first_total = frequency
    return first_total, first_repeat
