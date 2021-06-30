def frequency(display):
    display = display.split('\n')
    plus = 0
    minus = 0
    for number in display:
        if number[0] == '+':
            plus += int(number[1:])
        elif number[0] == '-':
            minus += int(number[1:])
    return plus - minus


with open('input.txt', 'r') as f:
    input_str = f.read()

print frequency(input_str)
