joltage = 0

def highest_num_task_one(inp):
    current_high = 0
    for i in range(len(inp)):
        first_digit = inp[i]

        for j in range(i + 1, len(inp)):
            second_digit = inp[j]
            cur_str_number = str(first_digit) + str(second_digit)
            cur_int_number = int(cur_str_number)
            if cur_int_number > current_high: current_high = cur_int_number;

    return current_high

def highest_num_task_two(number_str):
    num_to_remove = len(number_str) - 12
    
    stack = []
    removals_left = num_to_remove
    
    for digit in number_str:
        while stack and removals_left > 0 and stack[-1] < digit:
            stack.pop()
            removals_left -= 1
        
        stack.append(digit)
    
    while removals_left > 0:
        stack.pop()
        removals_left -= 1
    
    return ''.join(stack)

with open("input.txt") as file:
    for line in file:
        cur_line = line.rstrip()
        high = highest_num_task_two(cur_line)
        joltage += int(high)

print(f"joltage: {joltage}")
        
