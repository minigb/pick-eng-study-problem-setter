import pandas as pd
import datetime


today = datetime.date.today()
print(today)

def main():
    info = pd.read_csv('info.csv')

    bag = []
    for i in range(len(info)):
        if not info.loc[i, 'is_target']:
            continue

        last_date = info.loc[i, 'last_date']
        if not last_date:
            last_date = '2023-07-04'
        
        weeks_passed = (pd.to_datetime(datetime.date.today()) - pd.to_datetime(last_date)).days // 7

        today = datetime.date.today()
        print(today)

        
    
    for i in range(len(info)):
        last_date = info.loc[i, 'last_date']
        if not last_date:
            pass



if __name__ == '__main__':
    main()