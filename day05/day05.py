
def day05(inputs):
    ret = loop_reduce(inputs[0])

    ret2 = list()
    for letter_value in range(ord('A'), ord('Z') + 1):
        ret2.append(len(loop_reduce(reduce_input_by_letter(inputs[0], letter_value))))
    return len(ret), sorted(ret2)[0]


def loop_reduce(_input):
    ret = reduce_input(_input)
    while len(_input) != len(ret):
        _input = ret
        ret = reduce_input(_input)
    return ret


def reduce_input(_input):
    i = 0
    ret = list()
    while i + 1 < len(_input):
        if abs(ord(_input[i]) - ord(_input[i + 1])) - 32 != 0:
            ret.append(_input[i])
            i += 1
        else:
            i += 2
    ret.append(_input[-1])
    return ''.join(ret)


def reduce_input_by_letter(_input, letter_value):
    return ''.join([l for l in _input if ord(l) != letter_value and ord(l) - 32 != letter_value])
