from datetime import datetime

def whatTime():
    dmy = datetime.now()
    date = dmy.strftime('%d/%m/%Y')
    hour = dmy.strftime('%H:%M:%S')

    return date, hour

def get_dates():
    dmy = datetime.now()
    day = dmy.day
    month = dmy.month
    year = dmy.year

    return day, month, year


