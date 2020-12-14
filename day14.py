import pandas as pd
import numpy as np
import re

data = open('day14.txt').read().splitlines()

class bitmask:
    
    def __init__(self, mask):  
        self.mask = mask
        self.mask_list = self._get_mask_list(mask) 

    def _get_mask_list(self, mask):
        return [int(x) if x != 'X' else x for x in mask]
        
    def _get_binary_36(self, decimal):
        return bin(decimal)[2:]
        
    def apply_mask(self, decimal):
        
        mask_list_rev = self.mask_list[::-1]
        binary_rev = [x for x in str(self._get_binary_36(decimal)[::-1])]
        new_binary_rev = binary_rev + ['0'] * (len(mask_list_rev) - len(binary_rev))

        for i in range(0, len(mask_list_rev)):
            if mask_list_rev[i] != 'X':
                new_binary_rev[i] = str(mask_list_rev[i])
            else:
                continue
        
        new_binary = ''.join(new_binary_rev)[::-1]
        new_decimal = int(new_binary, 2)
        
        return new_decimal

    def apply_mask_float(self, decimal):

        mask_list_rev = self.mask_list[::-1]
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

    def get_all_decimals(self, decimal):

        float_result = self.apply_mask_float(decimal)
        
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

for entry in data:
    if entry.startswith('mask'):
        p = bitmask(entry[7:])
    else:
        mem_address = int(re.search(r"\[([0-9_]+)\]", entry).group(1))
        decimal = int(re.search(r"= ([0-9_]+)", entry).group(1))
        new_decimal = p.apply_mask(decimal)

        mem[mem_address] = new_decimal

print(sum(mem.values()))

# part 2
memm = {}

for entry in data:
    if entry.startswith('mask'):
        p1 = bitmask(entry[7:])
    else:
        mem_address = int(re.search(r"\[([0-9_]+)\]", entry).group(1))
        value = int(re.search(r"= ([0-9_]+)", entry).group(1))

        all_mem_address = p1.get_all_decimals(mem_address)

        for address in all_mem_address:
            memm[address] = value
        
print(sum(memm.values()))
