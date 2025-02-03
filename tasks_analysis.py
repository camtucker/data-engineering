import json
import pandas as pd
from datetime import datetime, timezone

# Load tasks from JSON
with open('output/tasks.json') as f:
    tasks = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(tasks)

# Ensure due dates are in datetime format with timezone awareness
df['due_date'] = pd.to_datetime(df['due'], errors='coerce', utc=True)

# Analysis Functions
def analyze_tasks(df):
    print("=== Task Analysis ===\n")

    # Total number of tasks
    total_tasks = len(df)
    print(f"Total tasks: {total_tasks}")

    # Count tasks by status
    status_counts = df['status'].value_counts()
    print("\nTasks by status:")
    print(status_counts)

    # Count tasks by task list
    if 'task_list' in df.columns:
        task_list_counts = df['task_list'].value_counts()
        print("\nTasks by task list:")
        print(task_list_counts)

    # Overdue tasks
    now = datetime.now(timezone.utc)  # Ensure current time is timezone-aware
    overdue_tasks = df[(df['due_date'] < now) & (df['status'] != 'completed')]
    print(f"\nOverdue tasks: {len(overdue_tasks)}")
    print(overdue_tasks[['title', 'due_date', 'status', 'task_list']].head(5))

# Run the analysis
if __name__ == "__main__":
    analyze_tasks(df)
