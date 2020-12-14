import pandas as pd
from math import ceil

data = open('day13.txt').read().splitlines()
timestamp = int(data[0])
schedule_x = [int(x) if x != 'x' else x for x in data[1].split(',')]


# part 1
df_schedule = pd.DataFrame([int(x) for x in data[1].split(',') if x != 'x'], columns=['bus'])

df_schedule['waiting_time'] =  df_schedule['bus'].apply(lambda x: x - (timestamp % x))
    
print(df_schedule['waiting_time'].min() * df_schedule['bus'][df_schedule['waiting_time'].idxmin()])

# part 2
df = pd.DataFrame(schedule_x, columns=['bus'])
df['t'] = [x for x in range(0, len(schedule_x))]

df = df[df['bus'] != 'x'].reset_index(drop=True)

def check_correct_t(time, next_bus, diff):
    if ((time) % next_bus) == 0:
        return True
    return False

a = True
# 100000000000000 / 19
i = 1895431131329359
first_bus = df['bus'][0]
while a:
    time = first_bus * i
    for j in range(1, (len(df['bus']))):
        check = check_correct_t(time, df['bus'][j], df['t'][j])
        if check:
            a = False
            continue
        elif not check:
            a = True
            i += 1
            break
    print(time)
        
print('Answer:', time)

# correct but will run for years;
 
