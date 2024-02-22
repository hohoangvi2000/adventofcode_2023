def calculate_value(list):
    dict = {
        'one': "1", 
        'two': "2", 
        'three': "3", 
        'four': "4", 
        'five': "5", 
        'six': "6", 
        'seven': "7", 
        'eight': "8", 
        'nine': "9"
    }
    store = []
    for line in list:
        digits = []
        for i, e in enumerate(line):
            if line[i].isdigit():
                digits.append(line[i])
            else:
                for k in dict.keys():
                    if line[i:].startswith(k):
                        digits.append(dict[k])
        if digits:
            value = int(digits[0]) * 10 + int(digits[-1])
            store.append(value)

    return sum(store)


input_file = open('day1_input.txt').readlines()
result = calculate_value(input_file)
print(result)



    

