import pandas as pd
import json
import datetime
import random
import time

TODAY = datetime.date.today()
START_DATE = '2023-07-04'


def read_info(file_name):
    if file_name.endswith('.csv'):
        return pd.read_csv(file_name)
    elif file_name.endswith('.json'):
        with open(file_name) as f:
            info = json.load(f)
            return pd.DataFrame.from_dict(info)
        

def refine_data(info):
    # Fill in the start date for those who don't have it
    info.loc[info['last_date'].isnull(), 'last_date'] = START_DATE
    # Fill in 'is_in_army' for those who don't have it
    info.loc[info['is_in_army'].isnull(), 'is_in_army'] = False
    # Fill in 'is_target' for those with 'is_in_army' as True
    info.loc[info['is_in_army'], 'is_target'] = False
    # Check if there's any missing value
    assert not info.isnull().values.any()
    # Check if last week's setter is updated
    last_week_date = (TODAY - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    assert last_week_date in set(info['last_date'])
    # Check if every value in info['last_date'] is later than START_DATE
    assert all(info['last_date'] > START_DATE)

    # If there's no target, set all non-army members as target
    if not info['is_target'].any():
        info.loc[info['is_in_army'] == False, 'is_target'] = True

    return info


def pick_setter(info):
    bag = []
    for i in range(len(info)):
        # Check if the person is a target
        if not info.loc[i, 'is_target']:
            continue
        assert info.loc[i, 'is_in_army'] == False

        # Put the person in the bag with the weight of weeks passed
        id = info.loc[i, 'id']
        last_date = info.loc[i, 'last_date']
        weeks_passed = (pd.to_datetime(TODAY) - pd.to_datetime(last_date)).days // 7
        bag.extend([id] * weeks_passed)

    random.shuffle(bag)
    random_pick = random.choice(bag)

    return random_pick


def give_suspense():
    for _ in range(2):
        time.sleep(0.8)
        print('.')
    time.sleep(2)


if __name__ == '__main__':
    info = read_info('info.json')
    info = refine_data(info)
    print('Targets: ', list(info[info['is_target']]['id']))

    setter = pick_setter(info)
    give_suspense()
    print("Next setter:", setter, '\U0001F389') # print with emoji