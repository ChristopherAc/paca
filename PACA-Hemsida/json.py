import json

def get_events():
    
    events = [
        {
        "title":"Event 1",
        "start": "2016-03-25",
        "end": "2016-03-25",
        "allDay": True,
        "color": "lightgreen"
    },
    {
        "title":"Event 2",
        "start": "2016-03-30 08:00:00",
        "end": "2016-03-30 10:30:00",
        "color": "gold"
    }

        ]
        
    return json.dumps(events)
