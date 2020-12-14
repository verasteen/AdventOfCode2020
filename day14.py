import pandas as pd
import numpy as np
import re

data = open('day14.txt').read().splitlines()

class bitmask:
    
    def __init__(self, mask):  
        self.mask_list = self._get_mask(mask) 
        self.mask = mask

    def _get_mask(self, mask):
        # mask = mask[::-1]
        return [int(x) if x != 'X' else x for x in mask]
        
    def _get_binary_36(self, decimal):
        return bin(decimal)[2:]
        

    def calculate_new_decimal(self, mask_list, decimal):
        
        mask_list_rev = mask_list[::-1]
        binary_rev = [x for x in str(self._get_binary_36(decimal)[::-1])]
        new_binary_rev = binary_rev + ['0'] * (len(mask_list_rev) - len(binary_rev))
        print(binary_rev)
        for i in range(0, len(mask_list_rev)):
            if type(mask_list_rev[i]) == int:
                new_binary_rev[i] = str(mask_list_rev[i])
            else:
                continue
        
        new_binary = ''.join(new_binary_rev)[::-1]
        new_decimal = int(new_binary, 2)
        
        return new_decimal

    def get_float_result(self, mask_list, decimal):

        mask_list_rev = mask_list[::-1]
        binary_rev = [x for x in str(self._get_binary_36(decimal)[::-1])]
        new_binary_rev = binary_rev + ['0'] * (len(mask_list_rev) - len(binary_rev))

        for i in range(0, len(mask_list_rev)):
            if mask_list_rev[i] == 1:
                new_binary_rev[i] = str(1)
            elif mask_list_rev[i] == 'X':
                new_binary_rev[i] = 'X'
            else:
                continue
        
        float_result = ''.join(new_binary_rev)[::-1]
        
        return float_result

def get_all_decimals(float_result):
    num_X = float_result.count('X')

    list_of_X_combi = [bin(x)[2:].zfill(num_X) for x in range(0, 2**num_X)]

    decimals = []
    for combi in list_of_X_combi:
        
        j = 0
        new_float = ''
        for i in float_result:
            if i == 'X':
                new_float += combi[j]
                j += 1
            else:
                new_float += i

        new_decimal = int(new_float, 2)
        decimals.append(new_decimal)

    return decimals


# part 1
mem = {}

for i in data:
    if i.startswith('mask'):
        p1 = bitmask(i[7:])
    else:
        mem_adress = int(re.search(r"\[([0-9_]+)\]", i).group(1))
        decimal = int(re.search(r"= ([0-9_]+)", i).group(1))
        new_decimal = p1.calculate_new_decimal(p1.mask_list, decimal)

        mem[mem_adress] = new_decimal

# print(sum(mem.values()))

# part 2
memm = {}

for i in data:
    if i.startswith('mask'):
        p1 = bitmask(i[7:])
    else:
        mem_adress = int(re.search(r"\[([0-9_]+)\]", i).group(1))
        value = int(re.search(r"= ([0-9_]+)", i).group(1))
        float_result = p1.get_float_result(p1.mask_list, mem_adress)
        all_mem_adress = get_all_decimals(float_result)

        for adress in all_mem_adress:
            memm[adress] = value
        
print(sum(memm.values()))
