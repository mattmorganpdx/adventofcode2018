
def day08(inputs):
    _input = list(map(int, inputs[0].split(' ')))
    _input2 = list(map(int, inputs[0].split(' ')))

    return get_meta_data(_input), get_root_value(_input2)


def get_meta_data(nodes, count=0):
    children = nodes.pop(0)
    md_count = nodes.pop(0)
    if children == 0:
        ret = sum([nodes.pop(0) for _ in range(md_count)])
        return ret
    else:
        sub_count = 0
        for _ in range(children):
            sub_count += get_meta_data(nodes, count)
        count += sum([nodes.pop(0) for _ in range(md_count)])
        count += sub_count
    return count


def get_root_value(nodes):
    children = nodes.pop(0)
    md_count = nodes.pop(0)
    if children == 0:
        return sum([nodes.pop(0) for _ in range(md_count)])
    else:
        node_map = {}
        for i in range(children):
            node_map[i+1] = get_root_value(nodes)
        md_list = [nodes.pop(0) for _ in range(md_count)]
        node_total = 0
        for i in md_list:
            if i in node_map:
                n = node_map[i]
                node_total += n
        return node_total
