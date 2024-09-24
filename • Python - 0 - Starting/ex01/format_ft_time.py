import time
import datetime

today = datetime.date.today()
timeStamp = time.time()
formatted_timeStamp = '{:,}'.format(float('{:.4f}'.format(timeStamp)))

print(f'Seconds since January 1, 1970: {formatted_timeStamp} or {'{:.2e}'.format(timeStamp)} in scientific notation')
print(today.strftime('%b'), today.day, today.year)