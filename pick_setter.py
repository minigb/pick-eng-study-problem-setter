import pandas as pd
import datetime
import random
import time

TODAY = datetime.date.today()
START_DATE = '2023-07-04'


def main():
    info = pd.read_csv('info.csv')

    bag = []
    for i in range(len(info)):
        if not info.loc[i, 'is_target']:
            continue

        id = info.loc[i, 'id']
        last_date = info.loc[i, 'last_date']
        if pd.isnull(last_date):
            last_date = START_DATE
        
        weeks_passed = (pd.to_datetime(TODAY) - pd.to_datetime(last_date)).days // 7
        bag.extend([id] * weeks_passed)

    if len(bag) == 0:
        bag = list(info['id'])

    random.shuffle(bag)
    random_pick = random.choice(bag)
    
    # Hold on for a while for suspense XD
    for i in range(2):
        time.sleep(0.8)
        print('.')
    time.sleep(2)
    
    # Print result
    print("Next setter:", random_pick, '\U0001F389') # print out with emoji
    time.sleep(1)

    
if __name__ == '__main__':
    main()