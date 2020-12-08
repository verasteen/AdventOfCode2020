import pandas as pd

data = pd.read_csv('day8.txt', sep=" ", header=None, engine='python', names=['action', 'number'])


# part 1

accumulator = 0
i = 0
used_instruction = []
while i not in used_instruction:
    instruction = data.loc[i]
    used_instruction.append(i)
    if instruction.action == 'jmp':
        i += instruction.number
    else:
        i += 1
        if instruction.action == 'acc':
            accumulator += instruction.number

print(accumulator)

# part 2

def check_if_terminates(df):
    highest_i = df.index.max()

    accumulator = 0
    i = 0
    used = []
    while i not in used:
        instruction = df.loc[i]
        used.append(i)
        if instruction.action == 'jmp':
            i += instruction.number
        else:
            i += 1
            if instruction.action == 'acc':
                accumulator += instruction.number
        
        if i > highest_i:
            return accumulator

    return False

# used_instructions of part 1 is the normal route
route = used_instruction

for j in route:
    action = data.loc[j].action

    if action == 'nop':
        data_copy = data.copy()
        data_copy['action'][j] = 'jmp' 

    elif action == 'jmp':
        data_copy = data.copy()
        data_copy['action'][j] = 'nop'

    else:
        continue

    accu = check_if_terminates(data_copy)

    if accu:
        print(accu)
        break
