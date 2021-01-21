from app import app
from flask import render_template, request
from app.models.event import Event
from app.models.event_list import events, add_event


@app.route('/events')
def index():
    return render_template("index.html", events=events)

@app.route('/events', methods=['POST'])
def add_new_event():
    event_date = request.form['date']
    event_name = request.form['name']
    event_guest = request.form['number_of_guest']
    event_location = request.form['location']
    event_desc = request.form['description']
    new_event = Event(event_date, event_name, event_guest, event_location, event_desc, False)
    add_event(new_event)
    return render_template ('index.html', events=events)


 
