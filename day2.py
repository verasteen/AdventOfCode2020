import pandas as pd 

data = pd.read_csv('day2.txt', sep=" ", header=None)

df = pd.DataFrame()

df['mini'] = data[0].apply(lambda x: int(x.split('-')[0]))
df['maxi'] = data[0].apply(lambda x: int(x.split('-')[1]))
df['letter'] = data[1].apply(lambda x: x.strip(':'))
df['password'] = data[2]

#part 1
def count_letter(pas, letter, mini, maxi):
    letters = pas.count(letter)  
    if letters >= mini and letters <= maxi:
        return 1
    else:
        return 0

df['correct'] = df.apply(lambda x: count_letter(x['password'], x['letter'], x['mini'], x['maxi']), axis=1)

print('answer:', sum(df.correct))


# part 2
def letter_position(pas, letter, mini, maxi):
    if pas[mini - 1] == letter and pas[maxi - 1] == letter:
        return 0
    elif pas[mini - 1] == letter or pas[maxi - 1] == letter:
        return 1
    else: 
        return 0

df['correct_2'] = df.apply(lambda x: letter_position(x['password'], x['letter'], x['mini'], x['maxi']), axis=1)
    
print('answer:', sum(df.correct_2))