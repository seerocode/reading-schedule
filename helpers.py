import pandas as pd
import numpy as np
import time
import datetime
from datetime import timedelta
import pprint
from collections import OrderedDict
import json

start_date = datetime.date(2020, 1, 6)

books_list = pd.read_csv('./data/books.csv')
bk_sorted = books_list.sort_values(by=['order'])

fun = 50 # reading for leisure 45-60 pages per hour
learn = 25 # reading for learning (highly technical or difficult reading) 15-30 pages to highlight and write notes 

# return how many days to finish book based on 
# reading type and number of pages
def calculate_days_to_read(pages, reading_type):
    if reading_type == 'fun':
        days = [pages, np.ceil(pages/fun)]
    if reading_type == 'learn':
        days = [pages, np.ceil(pages/learn)]
    return days

# create list based on calculate_days_to_read
# for page range each day per book (1 hour a day)
def daily_page_range(pages, reading_type):
    page_range = []
    date_pages = OrderedDict()
    dates_dict = OrderedDict()
    pages_dict = OrderedDict()
    page_speed = learn if reading_type == 'learn' else fun # multiply learn/fun by number of hours if desired
    rang = range(1, pages + 1, page_speed)
    global start_date
    curr_date = get_weekday(start_date)
    for begin in rang:
        if begin == pages:
            break
        if begin == rang[-1]:
            # create two dictionaries
            pg_range = '{} - {}'.format(begin, pages)
            pg_dates = curr_date.strftime("%m/%d/%Y, %H:%M:%S") # assign a day of week to page range 
            pages_dict['pages'] = pg_range
            dates_dict['date'] = pg_dates
            # add two dictionaries to a single array
            date_pages = {**pages_dict, **dates_dict}
        else:
            pg_range = '{} - {}'.format(begin, begin + page_speed)
            pg_dates = curr_date.strftime("%m/%d/%Y, %H:%M:%S") # assign a day of week to page range 
            pages_dict['pages'] = pg_range
            dates_dict['date'] = pg_dates
            date_pages = {**pages_dict, **dates_dict}
        curr_date += timedelta(days=1)
        curr_date = get_weekday(curr_date)
        start_date = curr_date
        page_range.append(date_pages)

    return page_range
        

def create_schedule(books):
    number_of_books = bk_sorted.shape[0]
    book_schedule = OrderedDict()
    for book in range(number_of_books):
        title = books['title'].iloc[book]
        pages = books['pages'].iloc[book]
        reading_type = books['type'].iloc[book]
        book_schedule[title] = daily_page_range(pages, reading_type)
    return book_schedule

# only get me weekdays
def get_weekday(start_date):
    current_date = start_date
    weekday = current_date.isoweekday()
    if weekday == 6: 
        current_date += datetime.timedelta(days=2)
    elif weekday == 7:
        current_date += datetime.timedelta(days=1)
    return current_date

schedule = create_schedule(bk_sorted)


with open('./data/data.json', 'w') as outfile:
    json.dump(OrderedDict(schedule), outfile)
