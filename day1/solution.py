
with open("input.txt") as inp_file:
    lines = inp_file.readlines()

eng_to_digit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}





sum = 0
for lidx, line in enumerate(lines):
    nums = []
    for idx, letter in enumerate(line):
        if letter.isdigit():
            nums.append(letter)
        else:  # Part 2
            for offset in range(1, 6):
                try:
                    if (digit := eng_to_digit.get(line[idx: idx + offset], None)):
                        nums.append(str(digit))
                except IndexError:
                    pass
    
    sum += int(nums[0] + nums[-1])

print(sum)


