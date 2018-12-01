def inverse_captcha(digits):
    output = 0
    if isinstance(digits, int):
        digits = str(digits)

    length = len(digits)
    for i, digit in enumerate(digits):
        if i != length - 1:
            if digits[i] == digits[i + 1]:
                output += int(digits[i])
        else:
            if digits[i] == digits[0]:
                output += int(digits[i])
    return output


for digit in [1122, 1111, 1234, 91212129]:
    print "digit %s: %s" % (digit, inverse_captcha(digit))

with open('input.txt') as f:
    numbers = f.read()

print "\nsolution: %s" % inverse_captcha(numbers)
