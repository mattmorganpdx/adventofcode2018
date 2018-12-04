import re
from collections import defaultdict
from collections import Counter


def day04(inputs):
    inputs = sorted(inputs)
    minutes_and_messages = list()
    for _input in inputs:
        minutes_and_messages.append(get_minute_and_message(_input))
    sleep_list = defaultdict(dict)
    current_guard = str()
    falls_asleep = int()
    for mm in minutes_and_messages:
        if 'Guard' in mm[1]:
            current_guard = int(re.search(r'\d+', mm[1]).group(0))
        if 'falls' in mm[1]:
            falls_asleep = int(mm[0])
        if 'wake' in mm[1]:
            current_guards_dict = sleep_list[current_guard]
            range_of_minutes = list(range(falls_asleep, int(mm[0])))
            try:
                curr_min = current_guards_dict['total_minutes']
                curr_dur = (int(mm[0]) - falls_asleep)
                current_guards_dict['total_minutes'] = curr_min + curr_dur
                current_guards_dict['minutes'] = current_guards_dict['minutes'] + range_of_minutes
            except Exception:
                current_guards_dict['total_minutes'] = int(mm[0]) - falls_asleep
                current_guards_dict['minutes'] = range_of_minutes
            sleep_list[current_guard] = current_guards_dict

    most_slept_minute = dict()
    for k, v in sleep_list.items():
        if v['minutes']:
            most_slept_minute[k] = {'time_slept': v['total_minutes'],
                                    'most_common_minute': Counter(v['minutes']).most_common(1)}
    sorted_by_most_time = sorted(most_slept_minute.items(), key=lambda x: x[1]['time_slept'], reverse=True)
    sorted_by_most_freq = sorted(most_slept_minute.items(), key=lambda x: x[1]['most_common_minute'][0][1],
                                 reverse=True)
    answer_1 = sorted_by_most_time[0][0] * sorted_by_most_time[0][1]['most_common_minute'][0][0]
    answer_2 = sorted_by_most_freq[0][0] * sorted_by_most_freq[0][1]['most_common_minute'][0][0]
    return answer_1, answer_2


def get_minute_and_message(_input):
    return _input.split(':')[1].split('] ')
