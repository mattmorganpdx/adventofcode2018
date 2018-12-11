import re
import matplotlib.pyplot as plt
from shared.utils import load_input


def day10(inputs):
    int_inputs = list()
    for _input in inputs:
        matches = re.findall(r'[\-0-9]+', _input)
        int_inputs.append(list(map(int, matches)))

    for e in range(10080, 10082, 1):
        xs = [i[0] + (i[2] * e) for i in int_inputs]
        ys = [i[1] + (i[3] * e) for i in int_inputs]
        plt.scatter(xs, ys)
        plt.show()
    return


if __name__ == "__main__":
    test_array = load_input('input')
    day10(test_array)
