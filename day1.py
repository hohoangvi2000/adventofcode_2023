def extract_calibration_values(list):
    total_sum = 0
    for line in list:
        digits = [int(char) for char in line if char.isdigit()]
        # print(digits)
        if len(digits) >= 1:
            calibration_value = digits[0] * 10 + digits[-1]
            # print(calibration_value)
        total_sum += calibration_value
    return total_sum

input_file = open('day1_input.txt').readlines()
result = extract_calibration_values(input_file)
print("The sum of calibration values is:", result)        
