import time

def getTime():
    date_full = {}

    date = time.strftime('%d %B %Y')
    t = time.strftime('%H:%M')

    date_full['time'] = t
    date_full['date'] = date

    return date_full

print(f"Time api: {getTime()}")


