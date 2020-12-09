import pandas as pd 

data = open('day9.txt').read().splitlines()
data = list(map(int, data))

preamble = 25

def check_if_valid(preamble_list, number):
    for num in preamble_list:
        if (number - num) in preamble_list:
            return True
    return False

# part 1
for i in range(preamble, (len(data))):
    preamble_list = data[(i-preamble):i]
    number = data[i]
    
    if not check_if_valid(preamble_list, number):
        invalid_number = number
        break

print(invalid_number)


# part 2

def find_cont_range(cont_list, invalid_number):
    if sum(cont_list) == invalid_number:
        return max(cont_list) + min(cont_list)
    return False

a = False
for i in range(0, len(data)):
    for j in range(i, len(data)):
        cont_list = data[i:j]
        answer = find_cont_range(cont_list, invalid_number)

        if answer:
            print(answer)
            a = True
            break
    if a:
        break