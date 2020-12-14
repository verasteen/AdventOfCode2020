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

        for i in range(0, len(mask_list_rev)):
            if type(mask_list_rev[i]) == int:
                new_binary_rev[i] = str(mask_list_rev[i])
            else:
                continue
        
        new_binary = ''.join(new_binary_rev)[::-1]
        new_decimal = int(new_binary, 2)
        
        return new_decimal

def update_mem(p1, decimal, mem_adress):
    new_decimal = p1.calculate_decimal(p1.mask, decimal)
    mem[mem_adress] = new_decimal

mem = {}

for i in data:
    if i.startswith('mask'):
        p1 = bitmask(i[7:])
    else:
        mem_adress = int(re.search(r"\[([0-9_]+)\]", i).group(1))
        decimal = int(re.search(r"= ([0-9_]+)", i).group(1))
        new_decimal = p1.calculate_new_decimal(p1.mask_list, decimal)

        mem[mem_adress] = new_decimal

print(sum(mem.values()))

