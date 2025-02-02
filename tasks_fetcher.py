from googleapiclient.discovery import build
import os
import json

def fetch_tasks(creds):
    try:
        service = build("tasks", "v1", credentials=creds)
        all_tasks = []
        page_token = None

        while True:
            tasks_result = service.tasks().list(
                tasklist='@default',
                maxResults=100,  # Set to the maximum allowed
                showCompleted=True,  # Include completed tasks
                showHidden=True,     # Include hidden tasks
                pageToken=page_token
            ).execute()

            tasks = tasks_result.get('items', [])
            all_tasks.extend(tasks)

            # Debug: Check if tasks are fetched
            print(f"Fetched {len(all_tasks)} tasks so far")

            page_token = tasks_result.get('nextPageToken')
            if not page_token:
                break

        # Get script directory and define output folder
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_folder = os.path.join(script_dir, 'output')
        output_file = os.path.join(output_folder, 'tasks.json')

        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)
        print(f"Saving files to: {output_file}")

        # Write tasks to JSON
        with open(output_file, 'w') as f:
            json.dump(all_tasks, f, indent=4)
        print(f"File saved successfully at {output_file}")

    except Exception as e:
        print(f"An error occurred while fetching tasks: {e}")
