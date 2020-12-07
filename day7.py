import pandas as pd

def count_bags(bag, content, df):
    con_lis = content.split(', ')
    for i in con_lis:
        if i[0] != 'n':
            df[i[2:-1]][bag] = int(i[0])

# data prep
data = pd.read_csv('day7.txt', sep=" bags contain ", header=None, engine='python', names=['bag', 'content'])

data['content'] = data['content'].str.replace('bags', '').str.replace('bag', '').str.replace('.', '')

df = pd.DataFrame(index=data['bag'], columns=data['bag'])    

_ = data.apply(lambda x: count_bags(x.bag, x.content, df), axis=1)

#part1

def find_bags(color, df=df, index='index'):
    bags = df.index[df[color] > 0].tolist()
    if len(bags) > 0:
        return bags
    return False

bags = ['shiny gold']
found_bags = []
while bags:
    new_bags = []
    for bag in bags:
        a = find_bags(bag)
        if a:
            new_bags += a    
        bags = new_bags
    found_bags.append(new_bags)

flat_list = [item for sublist in found_bags for item in sublist]

print(len(set(flat_list)))


#part2

def get_bag_num(color, num, df=df):
    bags = df.loc[color].dropna()
    bag_num = []
    for bag, amount in bags.iteritems():
        bag_num.append((bag, amount * num))
    
    return bag_num

bags = [('shiny gold', 1)]
found_bags = []

while bags:
    new_bags = []
    for bag in bags:
        a = get_bag_num(bag[0], bag[1])
        if a:
            new_bags += a  
        bags = new_bags
    found_bags.append(new_bags)

flat_list_two = [item for sublist in found_bags for item in sublist]

print(pd.DataFrame(flat_list_two)[1].sum())