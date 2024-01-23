import pandas as pd
import numpy as np
import datetime


TODAY = datetime.date.today()
START_DATE = '2023-07-04'

def main():
    info = pd.read_csv('info.csv')

    bag = []
    for i in range(len(info)):
        if not info.loc[i, 'is_target']:
            continue

        handle = info.loc[i, 'handle']
        last_date = info.loc[i, 'last_date']
        if pd.isnull(last_date):
            last_date = START_DATE
        
        weeks_passed = (pd.to_datetime(TODAY) - pd.to_datetime(last_date)).days // 7
        bag.append(handle * weeks_passed)

    

    
if __name__ == '__main__':
    main()