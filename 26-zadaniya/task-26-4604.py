with open('input.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse = True)

last_box = boxes[0]
count = 1

for box in boxes:
    if last_box - box >= 3:
        last_box = box
        count += 1

print(count, last_box)