import pandas as pd 
import re

data = open('day6.txt').read().split('\n\n')

df = pd.DataFrame([dat.replace('\n', '').split() for dat in data])

# part 1
df['unique_answer'] = df[0].apply(lambda x: len(set(x)) )

print(df['unique_answer'].sum())


# part 2
data_lists = [dat.replace('\n', ' ').split() for dat in data]

# count answers per group
df['answers'] = [len(dat) for dat in data_lists]

# make one list of group
df['list'] = [dat.replace('\n', '') for dat in data]

# create set
df['set'] = df['list'].apply(lambda x: list(set(x)))

def count_yes(se, li, answers):
    letter_count = 0
    yesses = 0
    for i in se:
        letter_count = li.count(str(i))

        if letter_count == answers:
            yesses += 1

    return yesses

# count each element of set in list
df['yes'] = df.apply(lambda x: count_yes(x.set, x.list, x.answers),axis=1)

print(df['yes'].sum())




