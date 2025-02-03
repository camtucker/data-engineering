from googleapiclient.discovery import build
import os
import json

# Fetch Tasks from All Task Lists
def fetch_tasks(creds):
    try:
        service = build("tasks", "v1", credentials=creds)
        all_tasks = []

        # Fetch all task lists
        task_lists_result = service.tasklists().list(maxResults=100).execute()
        task_lists = task_lists_result.get('items', [])

        for task_list in task_lists:
            task_list_id = task_list['id']
            task_list_title = task_list.get('title', 'Unknown List')

            print(f"Fetching tasks from list: {task_list_title}")

            page_token = None
            while True:
                tasks_result = service.tasks().list(
                    tasklist=task_list_id,
                    maxResults=100,
                    showCompleted=True,
                    showHidden=True,
                    pageToken=page_token
                ).execute()

                tasks = tasks_result.get('items', [])
                for task in tasks:
                    task['task_list'] = task_list_title  # Add task list info to each task

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


if __name__ == "__main__":
    creds = None  # Replace with your Google API credentials
    fetch_tasks(creds)
