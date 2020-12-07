import pandas as pd 

data = pd.read_csv('day1.txt', sep=" ", header=None)

data['2020'] = data.apply(lambda x: 2020 - x)
       
def x_in_column(x, column):
    """
    x is int
    column is pd.Series

    return int or False
    """
    
    if column.isin([x]).any().any(): 
        return ((2020 - x) * x)
    else:
        return False

# part 1
for i, row in data.iterrows():
    product = x_in_column(row[0], data['2020'])
    if product:
        print(product)
        break

# part2
def three_entries(data):
    for i, row in data.iterrows():
        for ix, rowx in data.iterrows():
            if data[0].isin( [(row['2020'] - rowx[0])] ).any().any() == True:
                answer = row[0] * rowx[0] * (row['2020'] - rowx[0])
                return answer
              



        
