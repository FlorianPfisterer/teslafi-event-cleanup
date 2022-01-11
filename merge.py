import csv
import glob

OUT_FILE_NAME = 'events-merged-15.csv'
CSV_FILES = glob.glob('data/*.csv')

SELECTED_PROPERTIES = [
    'Date',

    'speed',
    'latitude',
    'longitude',

    'est_battery_range',
    'charger_power',

    'outside_temp',
    'inside_temp',
    'driver_temp_setting',
    'passenger_temp_setting',
    'fan_status',
    'seat_heater_left',
    'seat_heater_right',
    'is_climate_on',
    'is_auto_conditioning_on'
]

# read all events
all_events = []
for file_name in CSV_FILES:
    with open(file_name, mode='r') as f:
        reader = csv.DictReader(f)
        all_events.extend(reader)

print(f'read {len(all_events)} events from {len(CSV_FILES)} files')

# filter events to include only those that have all selected properties
def remove_unused_properties(row):
    result = {}
    for property in SELECTED_PROPERTIES:
        if property not in row or row[property] == '':
            return None
        result[property] = row[property]   
    return result
        
filtered_events = list(filter(None, map(remove_unused_properties, all_events)))
print(f'got {len(filtered_events)} events after filtering')

if len(filtered_events) == 0:
    print('no events found, exiting')
    exit(0)

# write filtered events to CSV file
with open(OUT_FILE_NAME, mode='w') as f:
    writer = csv.DictWriter(f, filtered_events[0].keys())
    writer.writeheader()
    writer.writerows(filtered_events)

    print(f'wrote selected events to {OUT_FILE_NAME}')