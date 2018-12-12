power_level_map = dict()


def day11():
    for x in range(1, 301):
        for y in range(1, 301):
            power_level_map[(x, y)] = get_power_level((x, y))

    totals = list()
    highests = list()
    for s in range(3, 300):
        for x in range(1, 300):
            for y in range(1, 300):
                totals.append(get_section_total((x, y), size=s))
        local = sorted(totals, key=lambda x: x[0], reverse=True)[0]
        print(s, local)
        highests.append(local)

    return sorted(highests, key=lambda x: x[0], reverse=True)


def get_power_level(cell, sn=5719):
    return int(list(str((((cell[0] + 10) * cell[1]) + sn) * (cell[0] + 10)))[-3]) - 5


def get_section_total(cell, size=3):
    if cell[0] + size > 300 or cell[1] + size > 300:
        return 0, cell
    total = int()
    for x in range(cell[0], cell[0] + size):
        for y in range(cell[1], cell[1] + size):
            total += power_level_map[(x, y)]

    return total, cell


if __name__ == "__main__":
    print(day11())
