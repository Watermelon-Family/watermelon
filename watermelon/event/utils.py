from datetime import datetime, timedelta
from dateutil.parser import parse
import json


def create(filename, event_name='', priority=1) -> False:
    with open(filename, 'r', encoding='utf-8') as f:
        db = json.load(f)

    # checking 
    for event in db['todo']:
        if event['name'] == event_name:
            return False

    # writing
    event = {
        "name": event_name,
        "priority": priority,
        "use_time": 0,
        "create_time": str(datetime.now()),
        "finish_time": None
    }
    db['todo'].append(event)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=4)

    return True


def remove(filename, event_name='') -> bool:
    with open(filename, 'r', encoding='utf-8') as f:
        db = json.load(f)

    flag = False

    for idx, event in enumerate(db['todo']):
        if event['name'] == event_name:
            del db['todo'][idx]
            flag = True
            break

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=4)

    return flag


def finish(filename, event_name='') -> bool:
    with open(filename, 'r', encoding='utf-8') as f:
        db = json.load(f)

    flag = False

    for idx, event in enumerate(db['todo']):
        if event['name'] == event_name:
            event['finish_time'] = str(datetime.now())
            db['done'].append(event)
            del db['todo'][idx]
            flag = True
            break

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=4)

    return flag


def walk(filename, t, time) -> list:
    """

    :param filename:
    :param t: [tod | down]
    :param time: [day | week | month | year]
    :return: list
    """
    with open(filename, 'r', encoding='utf-8') as f:
        db = json.load(f)

    standard_time = None
    if time == 'day':
        standard_time = timedelta(days=1)
    elif time == 'week':
        standard_time = timedelta(weeks=1)
    elif time == 'month':
        standard_time = timedelta(weeks=4)
    elif time == 'year':
        standard_time = timedelta(weeks=52)

    events = []
    for event in db[t]:
        cur_time = event['create_time'] if t == 'todo' else event['finish_time']
        cur_time = parse(cur_time)
        if datetime.now() - cur_time <= standard_time:
            events.append(event)

    return events


def exist(filename, event_name) -> bool:
    with open(filename, 'r', encoding='utf-8') as f:
        db = json.load(f)

    for event in db['todo']:
        if event['name'] == event_name:
            return True

    return False


def modify_use_time(filename, event_name, add_time):
    with open(filename, 'r', encoding='utf-8') as f:
        db = json.load(f)

    for event in db['todo']:
        if event['name'] == event_name:
            event['use_time'] += add_time

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=4)