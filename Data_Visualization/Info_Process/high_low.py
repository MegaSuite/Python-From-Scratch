import csv
from anyio import current_default_worker_thread_limiter
import matplotlib.pyplot as plt
from datetime import datetime

filename='death_valley_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    # print(header_row)

    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)

    highs=[]
    dates=[]
    lows=[]

    for row in reader:
        current_date=datetime.strptime(row[0],"%Y-%m-%d")
        try:
            high=int(row[1])
            low=int(row[3])
            
        except ValueError:
            print(current_date,'missing data')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

    # Plot the high temperatures.

    fig=plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,highs,c='red',alpha=0.5)
    plt.plot(dates,lows,c='blue',alpha=0.5)
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1) # type: ignore


    # Format plot.

    title="Daily high and low temperatures - 2014\nSitka, AK"
    plt.title(title,fontsize=24)
    plt.xlabel('',fontsize=8)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)",fontsize=18)
    plt.tick_params(axis='both',labelsize=8)

    plt.show()