import json
import csv
from datetime import datetime, timedelta
import requests


session = requests.Session()

def initDates(start_date):

    dates = list()

    current_date = datetime.now().date()

    delta = timedelta(days=1)
    while start_date <= current_date:
        dates.append(start_date.strftime("%Y-%m-%d"))
        start_date += delta

    return dates

def getValues(initial_date, final_date):
    url = f'https://api.cambiocuba.money/api/v2/x-rates?msg=false&x_cur=CUP&date_from={initial_date}%2022:00:00&date_to={final_date}%2022:00:00'
    response = session.get(url)
    dicc = json.loads(response.text)
    if 'MLC.CUP' in dicc['statistics']:
        mlc_value = dicc['statistics']['MLC.CUP']['avg']
    else:
        mlc_value = 0.0
    if 'USD.CUP' in dicc['statistics']:
        usd_value = dicc['statistics']['USD.CUP']['avg']
    else:
        usd_value = 0.0
    return [mlc_value, usd_value]
