with open('input.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)

true_boxes = [boxes[0]]
for box in boxes:
    if true_boxes[-1] - box >= 3:
        true_boxes.append(box)

print(len(true_boxes), true_boxes[-1])