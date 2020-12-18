import re

data = open('day18.txt').read().split('\n')


def calculate(som):
    som_list = som.split()

    i = 1
    start_num = int(som_list[0])
    answer = start_num
    while i < (len(som_list) -1):
        if som_list[i] == '+':
            answer += int(som_list[i+1])
        elif som_list[i] == '*':
            answer *= int(som_list[i+1])
        i += 2

    return answer
# part1
final_answer = 0
for line in data:
    m = re.search(r"\(([+* 0-9_]+)\)", line)    
    while m:
        som = m[1]
        indexes = m.span()
        new_number = calculate(som)

        new_line = line[:indexes[0]] + str(new_number) + line[indexes[1]:]

        line = new_line
        m = re.search(r"\(([+* 0-9_]+)\)", line)

    final_answer += calculate(line)

print(final_answer)


# part 2
def calculate_addition(som):
    som_list = som.split()
    i = 1
    
    while '+' in som_list:
        if som_list[i] == '+':
            a = int(som_list[i-1]) + int(som_list[i+1])            
            answer = som_list[:i-1] + [str(a)] + som_list[i+2:]
            
            som_list = answer
            i = 1
        else:
            i += 2
    
    answer = calculate(' '.join(som_list))

    return answer


data = open('day18.txt').read().split('\n')
final_answer = 0
for line in data:
    m = re.search(r"\(([+* 0-9_]+)\)", line)    
    while m:
        som = m[1]
        indexes = m.span()
        new_number = calculate_addition(som)
        new_line = line[:indexes[0]] + str(new_number) + line[indexes[1]:]

        line = new_line
        m = re.search(r"\(([+* 0-9_]+)\)", line)

    final_answer += calculate_addition(line)

print(final_answer)   
        

