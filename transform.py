import csv

EVENTS_FILE_NAME = 'events-merged-15.csv'

with open(EVENTS_FILE_NAME, mode='r') as f:
    reader = csv.DictReader(f)
    events = list(reader)
    print(f'read {len(events)} events')

HISTORY_LENGTH = 5
TEMP_CHANGE_THRESHOLD = 1

for temp_thres in [0.0000001, 1, 2, 3, 4, 5]:
    samples = []
    previous_events = []
    for i in range(len(events)):
        event = events[i]

        if len(previous_events) != 0 and abs(float(previous_events[-1]['driver_temp_setting']) - float(event['driver_temp_setting'])) >= temp_thres:
            samples.append((previous_events.copy(), event))

        previous_events.append(event)
        if len(previous_events) > HISTORY_LENGTH:
            previous_events.pop(0)

    print(f'generated {len(samples)}\ samples with changes of at least {temp_thres}°K')

