import json
import pprint
from collections import OrderedDict
from models.event import Event

input_file = open('./data/data.json')
reading_schedule = json.load(input_file, object_hook=OrderedDict)
requests = []

def create_api_body(reading_schedule):
  for book in reading_schedule.keys():
    for i in reading_schedule[book]:
      book_pages = i['pages']
      book_date = i['date']
      summ = "Read pages {} in: [{}]".format(book_pages, book)
      event = Event(summ, book_date, book_date)
      body = event.create_event()
      requests.append(body)
  return requests

body = create_api_body(reading_schedule)

if __name__ == '__main__':
  with open('./data/body.json', 'w') as outfile:
      json.dump(body, outfile)