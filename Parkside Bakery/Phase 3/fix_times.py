#!/usr/bin/env python3
"""
Script to add 1 hour 49 minutes to specific bake task start times in the JSON file.
This fixes the oven scheduling conflict identified in the validation report.
"""

import json
import re
from datetime import datetime, timedelta

def add_time(time_str, minutes_to_add):
    """Add minutes to a time string in HH:MM format."""
    time_obj = datetime.strptime(time_str, "%H:%M")
    new_time = time_obj + timedelta(minutes=minutes_to_add)
    return new_time.strftime("%H:%M")

# Read the file
file_path = "/Users/jamie/Library/CloudStorage/GoogleDrive-onlinejamie74@gmail.com/My Drive/UAW Resources/Phase 3/parkside-bakery-complete-simulation.json"

with open(file_path, 'r') as f:
    content = f.read()

# Tasks that need time adjustment (add 109 minutes = 1h 49m)
# bake_031 through bake_040
tasks_to_update = {
    "bake_033": ("10:49", 109),
    "bake_034": ("11:12", 109),
    "bake_035": ("11:24", 109),
    "bake_036": ("11:32", 109),
    "bake_037": ("11:47", 109),
    "bake_038": ("12:02", 109),
    "bake_039": ("12:50", 109),
    "bake_040": ("13:02", 109),
}

# Apply time shifts
for task_id, (current_time, shift_minutes) in tasks_to_update.items():
    new_time = add_time(current_time, shift_minutes)
    # Find and replace the start time for this specific task
    pattern = f'("id": "{task_id}".*?"start": ")({current_time})(")'
    replacement = f'\\g<1>{new_time}\\g<3>'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    print(f"Updated {task_id}: {current_time} -> {new_time}")

# Write back
with open(file_path, 'w') as f:
    f.write(content)

print("\nTime shifts applied successfully!")
