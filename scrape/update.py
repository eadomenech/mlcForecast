import csv
from tools import initDates, getValues
from datetime import datetime, timedelta


with open('data.csv', "r", encoding="utf-8", errors="ignore") as scraped:
    final_line = scraped.readlines()[-1]

final_line_split = final_line.split(',')
data = [int(x) for x in final_line_split[0].split('-')]
initial_date = (datetime(data[0], data[1], data[2]) + timedelta(days=1)).date()

dates = initDates(initial_date)

with open('data.csv', 'a', encoding="utf-8", errors="ignore") as f:

    writer = csv.writer(f)

    for item, date in enumerate(dates[:-1]):
        data = list()
        data.append(date)
        data.extend(getValues(date, dates[item + 1]))
        # write the data
        print(data)
        writer.writerow(data)

    f.close()