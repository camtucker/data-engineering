from googleapiclient.discovery import build
import os
import json

def fetch_tasks(creds):
    service = build("tasks", "v1", credentials=creds)
    tasks_result = service.tasks().list(tasklist='@default').execute()
    tasks = tasks_result.get('items', [])

    # Output folder path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(script_dir, 'output')
    output_file = os.path.join(output_folder, 'tasks.json')

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Write tasks to JSON file
    with open(output_file, 'w') as f:
        json.dump(tasks, f, indent=4)

    print(f"Tasks saved to {output_file}")
