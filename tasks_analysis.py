import json
import pandas as pd
from datetime import datetime

# Load tasks from JSON
with open('output/tasks.json') as f:
    tasks = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(tasks)

# Ensure due dates are in datetime format
df['due_date'] = pd.to_datetime(df['due'], errors='coerce')

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

    # Overdue tasks
    now = datetime.utcnow()
    overdue_tasks = df[(df['due_date'] < now) & (df['status'] != 'completed')]
    print(f"\nOverdue tasks: {len(overdue_tasks)}")
    print(overdue_tasks[['title', 'due_date', 'status']].head(5))

# Run the analysis
if __name__ == "__main__":
    analyze_tasks(df)
