import pandas as pd 

data = pd.read_csv('day3.txt', sep=" ", header=None)

s = pd.Series(data[0])

len_row = len(s[0])
last_row = s.shape[0]

def check_tree(row, position):
    if position > (len_row - 1):
        position = position % len_row

    if row[position] == '.':
        return 0
    else:
        return 1

def count_trees(s, right, down):
    count = 0
    positionx = 0
    positiony = 0

    while positiony < last_row:

        count += check_tree(s[positiony], positionx)
        positionx += right
        positiony += down
    
    return count

# part 1
print(count_trees(s, 3, 1))

# part 2
answer = count_trees(s, 1,1) * count_trees(s, 3,1) * count_trees(s, 5,1) * count_trees(s, 7,1) * count_trees(s, 1,2)

print(answer)
