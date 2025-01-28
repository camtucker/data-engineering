from googleapiclient.discovery import build

def fetch_tasks(creds):
    service = build('tasks', 'v1', credentials=creds)
    tasklists = service.tasklists().list().execute()

    for tasklist in tasklists.get('items', []):
        print(f"\nTask List: {tasklist['title']}")
        tasks = service.tasks().list(tasklist=tasklist['id']).execute()
        for task in tasks.get('items', []):
            print(f"  - {task['title']} (Status: {task['status']})")
