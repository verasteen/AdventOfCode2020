import pandas as pd
from math import floor, ceil

data = pd.read_csv('day5.txt', header=None)

data['row_code'] = data[0].apply(lambda x: x[:7])
data['column_code'] = data[0].apply(lambda x: x[7:])

def find_place(mini, maxi, code):
    i = 0
    while mini != maxi:
        if code[i] == 'F' or code[i] == 'L':
            maxi -= ceil((maxi - mini) / 2)
        elif code[i] == 'B' or code[i] == 'R':
            mini += ceil((maxi - mini) / 2)
        i += 1

    return mini

# part 1

data['row'] = data['row_code'].apply(lambda x: find_place(0, 127, x))
data['column'] = data['column_code'].apply(lambda x: find_place(0, 7, x))

data['seat_id'] = data.apply(lambda x: (x.row * 8 + x.column), axis=1)

print(data['seat_id'].max())

# part 2
data = data.sort_values(by=['seat_id'])

data['diff'] = data['seat_id'].diff()

print(data[data['diff'] == 2]['seat_id'] - 1)

