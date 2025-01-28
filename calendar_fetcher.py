from googleapiclient.discovery import build
import os
import json

def fetch_calendar_events(creds):
    try:
        # Build the service
        service = build("calendar", "v3", credentials=creds)

        # Fetch events
        events_result = service.events().list(
            calendarId='primary', maxResults=10, singleEvents=True, orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])

        # Debug: Check if events are fetched
        print(f"Fetched {len(events)} events")

        # Get script directory and define output folder
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_folder = os.path.join(script_dir, 'output')
        output_file = os.path.join(output_folder, 'calendar_events.json')

        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)
        print(f"Saving files to: {output_file}")

        # Write events to JSON
        with open(output_file, 'w') as f:
            json.dump(events, f, indent=4)
        print(f"File saved successfully at {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
