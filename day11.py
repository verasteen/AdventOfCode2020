import pandas as pd

data = pd.read_csv('day11.txt', header=None)
df = data[0].apply(lambda x: pd.Series(list(x)))

num_row = len(df.index)
num_col = len(df.columns)

def get_range(row, column):
    range_row = [x for x in [(row - 1), row, (row + 1)] if (x >= 0 and x < num_row)]
    range_col = [x for x in [(column - 1), column, (column + 1)] if (x >= 0 and x < num_col)]
    return range_row, range_col

def become_occupied(row, column, df):
    """if no seat surrounding given seat is occupied, become occupied"""
    if df[column][row] != 'L':
        return df[column][row]

    range_row, range_col = get_range(row, column)

    for col in range_col:
        if sum(df[col][range_row] == '#') > 0:
            return df[column][row]
            break
    return '#'

def become_empty(row, column, df):
    """if more than 4 seats surrounding given seat are occupied, become empty"""
    if df[column][row] != '#':
        return df[column][row]

    range_row, range_col = get_range(row, column)
    
    seats_occu = 0
    for col in range_col:
        seats_occu += sum(df[col][range_row] == '#')

    # also count given seat (4 + 1)
    if seats_occu >= 5:
        return 'L'

    return df[column][row]

# count the # 
def count_occupied(df_copy):
    count = 0
    for i, col in df_copy.iteritems():
        count += sum(col == '#')
    return count


# part 1
df_copy = df.copy()
df_new = pd.DataFrame().reindex_like(df_copy)
a = True

while a:

    for i, col in df_copy.iteritems():
        for j, row in col.iteritems():
            df_new[i][j] = become_occupied(j, i, df_copy)

    df_copy = df_new.copy()

    for i, col in df_copy.iteritems():
        for j, row in col.iteritems():
            df_new[i][j] = become_empty(j, i, df_copy)

    if df_copy.equals(df_new):
        a = False
    else:
        df_copy = df_new.copy()

print('answer 1: ', count_occupied(df_copy))

# part 2
data = pd.read_csv('day11.txt', header=None)
df = data[0].apply(lambda x: pd.Series(list(x)))

num_row = len(df.index)
num_col = len(df.columns)



def get_directions(row, column):
    up = [(x, column) for x in range(0,row)]
    up.reverse()
    down = [(x, column) for x in range((row + 1), num_row)]
    left = [(row, x) for x in range(0, column)]
    left.reverse()
    right = [(row, x) for x in range((column + 1), num_col)]
    
    if row > column:
        max_x = column
        maxmax_x = num_col
        extra_x = row
    else:
        max_x = row
        maxmax_x = num_row
        extra_x = column

    up_left = [((row - x) , (column - x)) for x in range(1, (max_x + 1))]
    down_left = [((row + x) , (column - x)) for x in range(1, (maxmax_x - max_x))]

    up_right = [((row - x) , (column + x)) for x in range(1, (extra_x + 1))]
    down_right = [((row + x) , (column + x)) for x in range(1, (maxmax_x - max_x))]

    return up, down, left, right, up_left, down_left, up_right, down_right

def choose_seat_empty(row, column, empty, occupied, current_value):
    if current_value == '.':
        return current_value

    directions = get_directions(row,column)
    seen_occupied = 0
    for direct in directions:
        for d in direct:
            if d in empty:
                break
            elif d in occupied:
                seen_occupied += 1
                break
    if seen_occupied >= 5:
        return 'L'
    else:
        return current_value


def choose_seat_full(row, column, empty, occupied, current_value):
    if current_value != 'L':
        return current_value

    directions = get_directions(row,column)
    seen_occupied = 0
    for direct in directions:
        for d in direct:
            if d in empty:
                break
            elif d in occupied:
                seen_occupied += 1
                break
    if seen_occupied == 0:
        return '#'
    else:
        return current_value

df_copy = df.copy()
df_new = pd.DataFrame().reindex_like(df_copy)

a = True
x=0
while a:
    # make full
    x += 1
    print(x)
# get full
    occupied = []
    empty = []
    for i, col in df_copy.iteritems():
        for j, row in col.iteritems():
            if row == '#':
                occupied.append((j,i))
            elif row == 'L':
                empty.append((j,i))

    for i, col in df_copy.iteritems():
        for j, row in col.iteritems():
                df_new[i][j] = choose_seat_full(j, i, empty, occupied, row)

    df_copy = df_new.copy()

    # get empty
    occupied = []
    empty = []
    for i, col in df_copy.iteritems():
        for j, row in col.iteritems():
            if row == '#':
                occupied.append((j,i))
            elif row == 'L':
                empty.append((j,i))

    for i, col in df_copy.iteritems():
        for j, row in col.iteritems():
                df_new[i][j] = choose_seat_empty(j, i, empty, occupied, row)

    if df_copy.equals(df_new):
        a = False
    else:
        df_copy = df_new.copy()

  
print('answer 2:', count_occupied(df_copy))
