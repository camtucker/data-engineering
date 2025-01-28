from calendar_fetcher import fetch_calendar_events
from tasks_fetcher import fetch_tasks
from utils import authenticate_google

if __name__ == '__main__':
    SCOPES = [
        'https://www.googleapis.com/auth/calendar.readonly',
        'https://www.googleapis.com/auth/tasks.readonly'
    ]
    creds = authenticate_google('token.json', SCOPES)

    print("Fetching Google Calendar events...")
    fetch_calendar_events(creds)

    print("\nFetching Google Tasks...")
    fetch_tasks(creds)
