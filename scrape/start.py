from datetime import datetime
import csv
from tools import initDates, getValues

initial_date = datetime(2021, 1, 2).date()
header = ['date', 'MLC', 'USD']

with open('data.csv', 'w', encoding="utf-8", errors="ignore") as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    initial_date = datetime(2021, 1, 2).date()

    dates = initDates(initial_date)

    for item, date in enumerate(dates[:-1]):
        data = list()
        data.append(date)
        data.extend(getValues(date, dates[item + 1]))
        # write the data
        print(data)
        writer.writerow(data)

    f.close()
