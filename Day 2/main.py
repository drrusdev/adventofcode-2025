import re
total_invalid = 0

def return_factors(num):
    facs = []
    for i in range(1, num + 1):
        if num % i == 0:
            facs.append(i)
    return facs

def validate_id_task_one(inp):
    global total_invalid
    break_index = inp.index("-")
    id_start = int(inp[0:break_index])
    id_end = int(inp[break_index+1:])

    #print(f"inp: {inp}")
    #print(f"id_start: {id_start}")
    #print(f"id_end: {id_end}")
    
    for id_index in range(id_start, id_end + 1):
        str_index = str(id_index)
        if str_index[0] == "0":
            #print(f"found invalid by index 0: {id_index}")
            total_invalid += id_index
            
        elif len(str_index) % 2 == 0:
            str_first_half = str_index[0:int(len(str_index)/2)]
            str_second_half = str_index[int(len(str_index)/2):]
            #str_drp = str_index.count(str_half)
            #print(f"testing id_index {id_index} - str_first_half = {str_first_half}, str_second_half = {str_second_half}")
            #if str_drp > 1:
            if str_first_half == str_second_half:
                #print(f"found invalid by duplicate: {id_index}")
                total_invalid += id_index

def validate_id_task_two(inp):
    global total_invalid
    break_index = inp.index("-")
    id_start = int(inp[0:break_index])
    id_end = int(inp[break_index+1:])

    #print(f"inp: {inp}")
    #print(f"id_start: {id_start}")
    #print(f"id_end: {id_end}")
    
    for id_index in range(id_start, id_end + 1):
        str_index = str(id_index)
        if str_index[0] == "0":
            #print(f"found invalid by index 0: {id_index}")
            total_invalid += id_index
            continue

        index_factors = return_factors(len(str_index))
        #print(f"index_factors: {index_factors}")
        
        for factor in index_factors:
            if factor == len(str_index): 
                continue
            pattern = str_index[0:factor]
            #print(f"pattern: {pattern}")
            
            if pattern * (len(str_index) // factor) == str_index:
                #print(f"pattern found in index {str_index}!")
                total_invalid += id_index
                break  
                

with open("inputs.txt") as file:
    inputs = file.read()
    #filter data, couldnt be bothered reading as a csv and its not pythonic i dont care
    input_data = []
    filter_index = 0
    for i in range(len(inputs)):
        if inputs[i] == ",":
            new_append = inputs[filter_index:i]
            new_append = new_append.replace("\n", "")
            input_data.append(new_append)
            filter_index = i + 1

    input_data.append(inputs[filter_index:].replace("\n", ""))

    print(input_data)
    for filtered_inputs in input_data:
        validate_id_task_two(filtered_inputs)

    print(f"total_invalid: {total_invalid}")
    input("done!")
    
