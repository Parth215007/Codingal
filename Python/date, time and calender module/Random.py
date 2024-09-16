import random
import time

def getRandomDate(start_date,end_date):
    print("Start date is: ",start_date)
    print("\nEnd date is: ",end_date)
    x = random.random()
    date_format = '%m/%d/%Y'
    start_time = time.mktime(time.strptime(start_date, date_format))
    end_time = time.mktime(time.strptime(end_date, date_format))
    random_time = (start_time + x*(end_time-start_time))
    random_date = time.strftime(date_format,time.localtime(random_time))
    return random_date, random_time
print("Random date and random time are: ", getRandomDate('1/7/2024','7/2/2025'))




