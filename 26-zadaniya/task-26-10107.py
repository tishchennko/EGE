with open('input.txt.3.txt') as file:
    N = int(file.readline())
    events = [list(map(int, i.split())) for i in file]

events = sorted(events, key = lambda x: (x[1], -x[0]))

approved_events= [events[0]]
for event in events:
    if approved_events[-1][1] <= event[0]:
        approved_events.append(event)

print(len(approved_events), approved_events[-2:])
print(max(events[events.index(approved_events[-1]):]))