import pandas as pd 
import re

data = open('day4.txt').read().split('\n\n')
data = [dat.replace('\n', ' ').split() for dat in data]

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
field_optional = ['cid']

# create data frame
df = pd.DataFrame(index=[x for x in range(len(data))], columns=fields)
df_opt = pd.DataFrame(index=[x for x in range(len(data))], columns=field_optional)

def fill_df(row, entry):
    col, value = entry.split(':')
    
    if col in field_optional:
        df_opt[col].loc[row] = value
    else:
        df[col].loc[row] = value


# part 1
for i in range(len(data)):
    _ =[fill_df(i, x) for x in data[i]]

df['nan'] = df.isnull().any(axis=1)
df = df[df.nan == False]

print('Answer: ', len(df))

# part 2

eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def check_valid(row):
    if 1920 <= int(row.byr) <= 2002:
        if 2010 <= int(row.iyr) <= 2020:
            if 2020 <= int(row.eyr) <= 2030:
                if re.match(r'(\#)[a-f0-9]{6,}$', row.hcl):
                    if row.ecl in eye_colors:
                        if re.match(r'[0-9]' , row.pid) and len(row.pid) == 9:
                            if row.hgt.endswith('in'):
                                if 59 <= int(row.hgt[:-2]) <= 76:
                                    return True
                            elif row.hgt.endswith('cm'):
                                if 150 <= int(row.hgt[:-2]) <= 193:
                                    return True
                            else:
                                return False
    return False


df['valid'] = df.apply(lambda x: check_valid(x), axis=1)    

df = df[df.valid == True]

print('Answer: ', len(df))

