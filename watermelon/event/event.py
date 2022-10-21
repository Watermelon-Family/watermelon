import time
from operator import itemgetter
from prettytable import PrettyTable
from watermelon.event.utils import create, remove, finish, walk, exist, modify_use_time


def create_event(filename, event_info):
    event_name, priority = "", 1
    event_info = event_info.split(':')
    if len(event_info) == 0 or len(event_info) > 2:
        raise Exception('create event must input event name, illegal input')
    elif len(event_info) == 1:
        event_name = event_info[0]
    else:
        event_name = event_info[0]
        if event_info[1] == '':
            event_info[1] = '1'
        if not event_info[1].isdigit():
            raise Exception('priority must be a int type, illegal input')
        priority = int(event_info[1])

    create(filename, event_name, priority)


def remove_event(filename, event_name):
    remove(filename, event_name)


def finish_event(filename, event_name):
    finish(filename, event_name)


def list_event(filename, time):
    events = walk(filename, 'todo', time)
    events.sort(key=itemgetter('priority'), reverse=True)
    table = PrettyTable()
    table.field_names = ['name', 'priority', 'use time', 'create time']
    for event in events:
        table.add_row([event['name'], '⭐️' * event['priority'], '🍉' * ((event['use_time'] - 1) // 25 + 1),
                       event['create_time']])
    print(table)


def list_achievement(filename, time):
    events = walk(filename, 'done', time)
    events.sort(key=itemgetter('priority'), reverse=True)
    table = PrettyTable()
    table.field_names = ['name', 'priority', 'use time', 'finish time']
    for event in events:
        table.add_row([event['name'], '⭐️' * event['priority'], '🍉' * ((event['use_time'] - 1) // 25 + 1),
                       event['finish_time']])
    print(table)


def watermelon(filename, event_info):
    work_time, rest_time, event_name = 25, 5, ''
    event_info = event_info.split(':')

    if len(event_info) != 3:
        raise Exception('timer input illegal, please use work_time:rest_time:event_name')

    if len(event_info[0]) != 0:
        try:
            work_time = int(event_info[0])
        except Exception as e:
            raise Exception('work time must be int type')

    if len(event_info[1]) != 0:
        try:
            rest_time = int(event_info[1])
        except Exception as e:
            raise Exception('rest time must be int type')

    event_name = event_info[2]

    if not exist(filename, event_name):
        create_event(filename, event_name + ':1')

    # start self-discipline
    print('It is a time to work! 🍉')
    discipline(work_time)

    if rest_time > 0:
        print('It is a time to take a break! ☕️')
        discipline(rest_time)
    # end

    modify_use_time(filename, event_name, work_time)


def discipline(minutes):
    try:
        start_time = time.perf_counter()
        while True:
            use_second = int(round(time.perf_counter() - start_time))
            left_second = minutes * 60 - use_second

            if left_second < 0:
                print('')
                break

            count = f'{int(use_second) // 60}:{int(use_second) % 60} / {minutes}:00 🕑'
            progressbar(use_second, minutes * 60, minutes, count)
            time.sleep(1)
    except KeyboardInterrupt as e:
        print('\nHave a nice day! 🌴️')
        exit(0)


def progressbar(curr, total, duration=10, extra=''):
    frac = curr / total
    filled = round(frac * duration)
    print('\r', '🍉' * filled + '--' * (duration - filled), '[{:.0%}]'.format(frac), extra, end='')