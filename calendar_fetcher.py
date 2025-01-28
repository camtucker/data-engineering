import os
import json


def fetch_calendar_events(creds):
    service = build("calendar", "v3", credentials=creds)
    events_result = service.events().list(
        calendarId='primary', maxResults=10, singleEvents=True, orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])

    # Output folder path
    output_folder = 'output'
    output_file = os.path.join(output_folder, 'calendar_events.json')

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Write events to JSON file
    with open(output_file, 'w') as f:
        json.dump(events, f, indent=4)

    print(f"Calendar events saved to {output_file}")
