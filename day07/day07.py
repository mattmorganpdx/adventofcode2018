import re


def day07(inputs, workers=2):
    dep_pairs = list()
    for _input in inputs:
        dep_pairs.append(re.findall(r'(?<=\s)[A-Z]', _input))
    starting_letter = 'A'
    ordered_letters = list()
    starting_letter = find_first(dep_pairs, starting_letter)
    ordered_letters.append(starting_letter)
    unresolved = sorted(set([x[0] for x in dep_pairs] + [x[1] for x in dep_pairs]))
    dep_map = build_dep_map(dep_pairs)

    for letter in dep_map[starting_letter]['p']:
        ordered_letters = dig(letter, dep_map, ordered_letters)

    unresolved.remove(starting_letter)
    resolved = [starting_letter]
    dep_map = remove_all_parents(starting_letter, dep_map)
    while unresolved:
        for r in unresolved:
            if not dep_map[r]['c']:
                unresolved.remove(r)
                resolved.append(r)
                dep_map = remove_all_parents(r, dep_map)
                break

    dep_map = build_dep_map(dep_pairs)
    unresolved = sorted(set([x[0] for x in dep_pairs] + [x[1] for x in dep_pairs]))
    resolved2 = []
    inprogress = dict()
    counter = 0
    while unresolved:
        for r in unresolved:
            if not dep_map[r]['c'] and r not in inprogress:
                if len(inprogress) < workers:
                    inprogress[r] = ord(r) - 4
        for t in list(sorted(inprogress.keys(), reverse=True)):
            inprogress[t] += -1
            if inprogress[t] == 0:
                inprogress.pop(t)
                unresolved.remove(t)
                resolved2.append(t)
                dep_map = remove_all_parents(t, dep_map)
        counter += 1

    return ''.join(resolved), counter


def build_dep_map(dep_pairs):
    dep_map = dict()
    for i in sorted(set([x[0] for x in dep_pairs] + [x[1] for x in dep_pairs])):
        dep_map[i] = dict()
        dep_map[i]['p'] = sorted([k[1] for k in dep_pairs if k[0] == i])
        dep_map[i]['c'] = sorted([k[0] for k in dep_pairs if k[1] == i])
    return dep_map


def remove_all_parents(letter, dep_map):
    for k in dep_map:
        if letter in dep_map[k]['c']:
            dep_map[k]['c'].remove(letter)
    return dep_map


def dig(letter, dep_map, resolved, q=[]):
    if not dep_map[letter]['p']:
        resolved.append(letter)
        return resolved

    for kid in dep_map[letter]['c']:
        if kid not in resolved:
            resolved = dig(kid, dep_map, resolved)
    return resolved


def find_first(dep_pairs, starting_letter):
    while True:
        next_letter = filter_letter(starting_letter, dep_pairs)
        if next_letter:
            starting_letter = next_letter
        else:
            break
    return starting_letter


def find_next(dep_pairs, starting_letter):
    while True:
        next_letter = find_deps(starting_letter, dep_pairs)
        if next_letter:
            starting_letter = next_letter
        else:
            break
    return starting_letter


def filter_letter(letter, pairs):
    deps = sorted([e[0] for e in filter(lambda x: x[1] == letter, pairs)])
    return deps[0] if len(deps) > 0 else None


def find_deps(letter, pairs):
    deps = sorted([e[1] for e in filter(lambda x: x[0] == letter, pairs)])
    return deps[0] if len(deps) > 0 else None
