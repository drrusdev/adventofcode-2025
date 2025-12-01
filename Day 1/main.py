import operator
cur_value = 50
total_hits_zero = 0

ops = {
    "L": operator.sub,
    "R": operator.add
}

def calculate_task_one(inp):
    global cur_value
    global total_hits_zero

    #print(f"current inp: {inp}")
    move_type = inp[0]
    value = int(inp[1:])
    op_func = ops[move_type]
    new_value = op_func(cur_value, value) % 100
    #print(f"new_value: {new_value}")
    total_hits_zero += int(new_value == 0) or int(new_value == 100)
    return new_value

def calculate_task_two(inp):
    global cur_value
    global total_hits_zero
    
    move_type = inp[0]
    value = int(inp[1:])
    op_func = ops[move_type]
    new_value = op_func(cur_value, value)
    
    if cur_value != 0:
        if move_type == "L":
            if value >= cur_value:
                total_hits_zero += 1 + ((value - cur_value) // 100)
        else:
            steps_to_zero = 100 - cur_value
            if value >= steps_to_zero:
                total_hits_zero += 1 + ((value - steps_to_zero) // 100)
    else:
        total_hits_zero += value // 100
    
    cur_value = new_value % 100
    return cur_value


with open("inputs.txt") as moves:
    for line in moves:
        #print(line)
        cur_value = calculate_task_two(line.strip())
        #print(cur_value)

print(f"cur_value: {cur_value}")
print(f"total_hits_zero {total_hits_zero}")
    
        
