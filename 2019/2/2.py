import math

def calculate_mass(numbers):
    nums = numbers.split('\n')
    nums = [math.floor(int(num) / 3) - 2 for num in nums if num != '']
    return int(sum(nums))

with open('input.txt', 'r') as f:
    input_str = f.read()

print calculate_mass(input_str)
