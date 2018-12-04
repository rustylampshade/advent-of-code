import re

with open('inputs/4_1.txt', 'r') as aoc_input:
    logs = aoc_input.read().rstrip('\n').split('\n')
    logs.sort()

def add_sleeping_minutes(ds, guard, date, start, stop):
    if not start[0]:
        return
    if guard not in ds:
        ds[guard] = {}
    if date not in ds[guard]:
        ds[guard].update({date: range(int(start[1]), int(stop[1]))})
    else:
        ds[guard][date].extend(range(int(start[1]), int(stop[1])))

tracker = {}
re_guard = re.compile(r'\[([0-9-]+) (\d+):(\d+)\] Guard #(\d+) begins shift')
re_sleep = re.compile(r'\[([0-9-]+) (\d+):(\d+)\] falls asleep')
re_wake = re.compile(r'\[([0-9-]+) (\d+):(\d+)\] wakes up')
for entry in logs:
    match = re.match(re_guard, entry)
    if match:
        # A new day, clear the old data.
        sleep_date, sleep_hour, sleep_minute, wake_date, wake_hour, wake_minute = [None] * 6
        start_date, start_hour, start_minute, guard = match.groups()
        continue
    
    match = re.match(re_sleep, entry)
    if match:
        sleep_date, sleep_hour, sleep_minute = match.groups()
        continue

    match = re.match(re_wake, entry)
    if match:
        wake_date, wake_hour, wake_minute = match.groups()
        add_sleeping_minutes(tracker, guard, wake_date, (sleep_hour, sleep_minute), (wake_hour, wake_minute))
        continue

# PART 1 

total_sleep = {}
for guard in tracker.keys():
    total_sleep[guard] = sum([len(sleep_minutes) for sleep_minutes in tracker[guard].values()])
snooziest_guard = max(total_sleep, key=total_sleep.get)
print 'Guard {0} slept the most, with {1} minutes'.format(snooziest_guard, total_sleep[snooziest_guard])

minutes = {}
for slept in tracker[snooziest_guard].values():
    for single_minute in slept:
        if single_minute not in minutes:
            minutes[single_minute] = 1
        else:
            minutes[single_minute] += 1

snooziest_minute = max(minutes, key=minutes.get)
print 'Of those minutes, minute #{0} was snoozed the most often'.format(snooziest_minute)
print 'Final answer: {0}'.format(int(snooziest_guard) * int(snooziest_minute))

# PART 2

minutes = {}
highest_count = 0
highest_minute = None
highest_guard = None
for guard, dates in tracker.items():
    minutes[guard] = {}
    for date in dates:
        for single_minute in tracker[guard][date]:
            if single_minute not in minutes[guard]:
                minutes[guard][single_minute] = 1
            else:
                minutes[guard][single_minute] += 1
    this_highest_minute = max(minutes[guard], key=minutes[guard].get)
    if minutes[guard][this_highest_minute] > highest_count:
        highest_count = minutes[guard][this_highest_minute]
        highest_minute = this_highest_minute
        highest_guard = guard
print 'Guard {0} snoozed on minute {1} more often than anyone else, with {2}'.format(highest_guard, highest_minute, highest_count)
print 'Final answer: {0}'.format(int(highest_guard) * int(highest_minute))