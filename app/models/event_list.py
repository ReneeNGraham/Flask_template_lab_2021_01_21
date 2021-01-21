from app.models.event import *
import datetime

event1 = Event (1-1-2020, "music festival", 1000, "room1", "alternative music", True)
event2 = Event (2-2-2020, "birthday party", 14, "room2", "40th celebration", True)
event3 = Event (3-2-2020, "business meeting", 7, "room3", "covid meeting", False)

events = [event1, event2, event3]

def add_event(event):
    events.append(event)

def remove_event(event):
    events.remove(event)

