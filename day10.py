import pandas as pd
import numpy as np

data = pd.read_csv('day10.txt', names=['joltage'])

built_in_adapter = data['joltage'].max() + 3
charging_outlet = 0

data.loc['charging_outlet'] = charging_outlet

joltages = data.joltage.values 
joltages = np.append(joltages, built_in_adapter)
   
def find_adapter(current_joltage, joltages=joltages):
    i = 1
    while (current_joltage + i) not in joltages:
        i += 1
    return (current_joltage + i)
            
# part 1

data['joltage_next_adapter'] = data['joltage'].apply(lambda x: find_adapter(x, joltages))
data['difference'] = data['joltage_next_adapter'] - data['joltage']

one_jolt_diff = len(data[data['difference'] == 1.0])
three_jolt_diff = len(data[data['difference'] == 3.0])
            
print(one_jolt_diff * three_jolt_diff)

# part 2
def find_all_adapter(current_joltage, joltages=joltages):
    next_adapaters = []
    i = 1
    while i < 4:
        if (current_joltage + i) in joltages:
            next_adapaters.append((current_joltage + i))
        i += 1
    return next_adapaters

def find_all_differences(current_joltage, joltages=joltages):
    differences = []
    i = 1
    while i < 4:
        if (current_joltage + i) in joltages:
            differences.append((i))
        i += 1
    return differences

data['all_next_adapter'] = data['joltage'].apply(lambda x: find_all_adapter(x, joltages))
data['all_differences'] = data['joltage'].apply(lambda x: find_all_differences(x, joltages))
data['number_adapter'] = data['all_next_adapter'].apply(lambda x: len(x))
data = data.sort_values(by=['joltage']).reset_index(drop=True)


def reach_adap(current_joltage, joltages=joltages):
    prev_adapaters = []
    i = 1
    while i < 4:
        if (current_joltage - i) in joltages:
            prev_adapaters.append((current_joltage - i))
        i += 1
    if len(prev_adapaters) > 0:
        return prev_adapaters    
    return False



end_jolt = data['joltage'].max() + 3

adapters = [end_jolt]
num_reach = []
prev_adap = []

while adapters:
    num_reach.append((prev_adap))
    prev_adap = []
    for adap in adapters:
        a = reach_adap(adap, joltages)
        if a:
            prev_adap += a
    adapters = prev_adap

print(max(num_reach))

flat_list = [item for sublist in num_reach for item in sublist]

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

