import pandas as pd

data = pd.read_csv('day12.txt', header=None)
df = pd.DataFrame()
df['action'] = data[0].apply(lambda x: x[0])
df['value'] = data[0].apply(lambda x: int(x[1:]))

def facing_direction(current_degree, action, value):
    if action == 'L':
        current_degree -= value
    elif action == 'R':
        current_degree += value

    if current_degree < 0:
        return 360 + current_degree
    elif current_degree >= 360 and current_degree < 720:
        return current_degree - 360
    elif current_degree == 720:
        return 0
    return current_degree

north = 0
east = 0

start_degree = 90
current_degree = start_degree

for i, row in df.iterrows():
    if row.action == 'L' or row.action == 'R':
        current_degree = facing_direction(current_degree, row.action, row.value)

    elif row.action == 'F':
        if current_degree == 0:
            north += row.value
        elif current_degree == 90:
            east += row.value
        elif current_degree == 180:
            north -= row.value
        elif current_degree == 270:
            east -= row.value
    
    elif row.action == 'N':
        north += row.value
    elif row.action == 'E':
        east += row.value
    elif row.action == 'S':
        north -= row.value
    elif row.action == 'W':
        east -= row.value
    
print(abs(north) + abs(east))

        
# part 2

def facing_waypoint(waypoint_n, waypoint_e, action, value):
    
    if action == 'N':
        waypoint_n += value
    elif action == 'E':
        waypoint_e += value
    elif action == 'S':
        waypoint_n -= value
    elif action == 'W':
        waypoint_e -= value

    return waypoint_n, waypoint_e

def turn_waypoint(waypoint_n, waypoint_e, action, value):
    if abs(value) == 90:
        if action == 'L':
            new_waypoint_n = waypoint_e
            new_waypoint_e = -waypoint_n
        elif action == 'R':
            new_waypoint_n = -waypoint_e
            new_waypoint_e = waypoint_n

    elif abs(value) == 180:
        new_waypoint_n = -waypoint_n
        new_waypoint_e = -waypoint_e
    elif abs(value) == 270:
        if action == 'R':
            new_waypoint_n = waypoint_e
            new_waypoint_e = -waypoint_n
        elif action == 'L':
            new_waypoint_n = -waypoint_e
            new_waypoint_e = waypoint_n

    return new_waypoint_n, new_waypoint_e

x = 1
y = 10

north = 0
east = 0

for i, row in df.iterrows(): 

    if row.action == 'L' or row.action == 'R':
        x, y = turn_waypoint(x, y, row.action, row.value)

    elif row.action == 'F':
        north += (row.value * x)
        east += (row.value * y)

    else:
        x, y = facing_waypoint(x, y, row.action, row.value)


print(abs(north) + abs(east))
