import numpy as np

data = open('day15.txt').read().split(',')

numbers = np.array([int(x) for x in data])
new_number = 0

while len(numbers) != 30000000:
    last_number = numbers[-1]
    spoken_on = np.where(numbers == last_number)[0]

    if len(spoken_on) < 2:
        new_number = 0
    elif len(spoken_on) >= 2:
        new_number = spoken_on[-1] - spoken_on[-2]

    numbers = np.append(numbers, new_number)

print(new_number)


## part 2 - same but faster
pos_1 = dict(zip(data, [x for x in range(1, (len(data) + 1))]))
pos_2 = {}

last_spoken_number = data[-1]
turn = len(data) + 1

while turn != 30000001:
    
    if last_spoken_number in pos_2:
        new_number = pos_1[last_spoken_number] - pos_2[last_spoken_number]
    else:
        new_number = 0

    if new_number in pos_1:
        pos_2[new_number] = pos_1[new_number]
        pos_1[new_number] = turn
    else:
        pos_1[new_number] = turn

    turn += 1
    last_spoken_number = new_number

print(new_number)

