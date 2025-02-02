import json
import pandas as pd
from datetime import datetime

# Load calendar events from JSON
with open('output/calendar_events.json') as f:
    events = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(events)

# Ensure date columns are in datetime format
df['start_time'] = pd.to_datetime(df['start'].apply(lambda x: x.get('dateTime') if x else None))
df['end_time'] = pd.to_datetime(df['end'].apply(lambda x: x.get('dateTime') if x else None))

# Analysis Functions
def analyze_calendar_events(df):
    print("=== Calendar Events Analysis ===\n")

    # Total number of events
    total_events = len(df)
    print(f"Total events: {total_events}")

    # Count events by type (simple keyword search in summary)
    keywords = ['Meeting', 'Call', 'Review', 'Workshop']
    for keyword in keywords:
        count = df['summary'].str.contains(keyword, case=False, na=False).sum()
        print(f"Number of '{keyword}' events: {count}")

    # Upcoming events
    now = datetime.utcnow()
    upcoming_events = df[df['start_time'] > now]
    print(f"\nUpcoming events: {len(upcoming_events)}")
    print(upcoming_events[['summary', 'start_time', 'end_time']].head(5))

# Run the analysis
if __name__ == "__main__":
    analyze_calendar_events(df)
