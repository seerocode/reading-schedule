import json
import constants
import pprint
from  collections import OrderedDict


# reading_schedule = {}
# with open('./data/data.json') as data:
#     reading_schedule = json.load(data, object_hook=OrderedDict)

input_file = open('./data/data.json')
reading_schedule = json.load(input_file)

def create_api_body(summ, start, end):
    email = constants.email

    summary = summ
    start_time = start
    end_time = end
    time_zone = 'America/New_York'

    body = {
        "summary": summary,
        "start": {
            "dateTime": start_time,
            "timeZone": time_zone,
        },
        "end": {
            "dateTime": end_time,
            "timeZone": time_zone,
        },
        'reminders': {
          'useDefault': False,
          'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
          ],
      }
    }

    return body

def stuff(reading_schedule):
  summ = ''
  start = ''
  end = ''
  for book in reading_schedule.keys():
    title = book

    print('title', title)
    summ = Read 
    for pages in book[0].keys:
        # summ = 'read pages ' + date + ' in ' + title
        print(summ)
        start = date
        print(start)
        end = date
        print(end)


# stuff(reading_schedule)
# print(type(reading_schedule))

# print(list(reading_schedule['Where the Crawdads Sing'][0].keys()))
# print(list(reading_schedule['Where the Crawdads Sing'][0].values()))
# print(list(reading_schedule['Where the Crawdads Sing'][0]))

# for key,val in list(reading_schedule['Where the Crawdads Sing'].items()):
#   print(key, "=>", val)

# for i in list(reading_schedule['Where the Crawdads Sing'][0].keys()):
#   print(i)

print(reading_schedule[0][0])



