import pprint

class Event:
  def __init__(self, summary, start, end):
    self.summary = summary
    self.start = start
    self.end = end

  def create_event(self):
    event = {
  'summary': self.summary,
  'start': {
    'dateTime': self.start,
    'timeZone': 'America/New_York',
  },
  'end': {
    'dateTime': self.end, #The date, in the format "yyyy-mm-dd", if this is an all-day event.
    'timeZone': 'America/New_York',
  },
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],              
  },
}

    return event


