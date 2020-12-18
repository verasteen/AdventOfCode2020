import numpy as np
import pandas as pd

data = open('day16.txt').read().split('\n\n')

rules = data[0].split('\n')
my_ticket = data[1].split('\n')
nearby_tickets = data[2].split('\n')[1:]

# rules
rules_list = []
for rule in rules:
    rule_name = rule.split(': ')[0]
    rule_values = rule.split(': ')[1]
    rule_tuple = ( rule_name,
                    int(rule_values.split(' or ')[0].split('-')[0]),
                    int(rule_values.split(' or ')[0].split('-')[1]), 
                    int(rule_values.split(' or ')[1].split('-')[0]), 
                    int(rule_values.split(' or ')[1].split('-')[1]) )
    rules_list.append(rule_tuple)

df_rules = pd.DataFrame(rules_list,columns=['field', 'min_one', 'max_one', 'min_two', 'max_two'])


# valid values
valid_values = {}
for i, row in df_rules.iterrows():
    for j in range(row.min_one, (row.max_one + 1)):
        valid_values[j] = 'valid'

    for k in range(row.min_two, (row.max_two + 1)):
        valid_values[k] = 'valid'


## part 1
invalid_numbers = []
for ticket in nearby_tickets:
    invalid = [int(x) for x in ticket.split(',') if int(x) not in valid_values]
    if invalid:
        invalid_numbers += invalid
 
print(sum(invalid_numbers))
    

## part 2
valid_tickets = []
for ticket in nearby_tickets:
    invalid = [int(x) for x in ticket.split(',') if int(x) not in valid_values]
    if not invalid:
        valid_tickets.append([int(x) for x in ticket.split(',')])
df_tickets = pd.DataFrame(valid_tickets)


possibilities = {}
for column in range(0, df_tickets.shape[1]):
    fields = []
    for i, row in df_rules.iterrows():
        
        valid_values = {}
        for j in range(row.min_one, (row.max_one + 1)):
            valid_values[j] = 'valid'

        for k in range(row.min_two, (row.max_two + 1)):
            valid_values[k] = 'valid'
        
        check = df_tickets[column].apply(lambda x: True if x in valid_values else False)
        
        if check.all() == True:
            fields.append(row.field)

    possibilities[column] = fields
            
keys = list(possibilities.keys())
values = list(possibilities.values())
len_values = np.array([len(x) for x in values])

solution = {}
values_copy = values
while len(solution) != len(values):
    len_values = np.array([len(x) for x in values_copy])
    
    index_one = np.where(len_values == 1)[0][0]
    solution[values_copy[index_one][0]] = index_one

    new_values = [[ele for ele in sub if ele != values_copy[index_one][0]] for sub in values_copy]

    values_copy = new_values

print(solution['departure date'])
print(solution['departure track'])
print(solution['departure platform'])
print(solution['departure station'])
print(solution['departure time'])
print(solution['departure location'])

# some manual steps
