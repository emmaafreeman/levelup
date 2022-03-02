"""Module for generating events by user report"""
import sqlite3
from django.shortcuts import render
from levelupapi.models import Gamer, Event
from levelupreports.views import Connection


def userevent_list(request):
    """Function to build an HTML report of events by user"""
    if request.method == 'GET':
        # Connect to project database
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # Query for all games, with related user info.
            db_cursor.execute("""
                SELECT
                    g.id,
                    g.user_id,
                    e.description,
                    e.date,
                    e.time,
                    e.game_id,
                    e.organizer_id,
                    u.id user_id,
                    u.first_name || ' ' || u.last_name AS full_name
                FROM
                    levelupapi_gamer g
                JOIN
                    levelupapi_gamer_sign_up_events su ON su.gamer_id = g.id
                JOIN
                    levelupapi_event e ON su.event_id = e.id
                JOIN 
                    auth_user u ON g.user_id = u.id
            """)

            dataset = db_cursor.fetchall()

            events_by_user = {}

            for row in dataset:
                # Create a Gamer instance and set its properties
                event = Event()

                event.description = row["description"]
                event.date = row["date"]
                event.time = row["time"]
                event.game_id = row["game_id"]
                event.organizer_id = row["organizer_id"]
                
                # Store the user's id
                uid = row["user_id"]

                # If the user's id is already a key in the dictionary...
                if uid in events_by_user:

                    # Add the current gamer to the `gamers` list for it
                    events_by_user[uid]['events'].append(event)

                else:
                    # Otherwise, create the key and dictionary value
                    events_by_user[uid] = {}
                    events_by_user[uid]["id"] = uid
                    events_by_user[uid]["full_name"] = row["full_name"]
                    events_by_user[uid]["events"] = [event]

        # Get only the values from the dictionary and create a list from them
        list_of_users_with_events = events_by_user.values()

        # Specify the Django template and provide data context
        template = 'users/list_with_events.html'
        context = {
            'userevent_list': list_of_users_with_events
        }

        return render(request, template, context)