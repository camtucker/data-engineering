from googleapiclient.discovery import build

def fetch_calendar_events(creds):
    service = build('calendar', 'v3', credentials=creds)
    events_result = service.events().list(
        calendarId='primary', maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(f"{start} - {event['summary']}")
