with open(r"C:\Users\alias\Desktop\dev\aoc-23\day3\input.txt") as inp_file:
    lines = inp_file.readlines()





parts = []

def check_column(col, start_row, end_row):
    for row in range(start_row, end_row + 1):
        slot = lines[row][col]
        print(row, col, slot, slot != "." and not slot.isdigit())
        if slot != "." and not slot.isdigit() and slot != "\n":
            return True
    return False

for row, line in enumerate(lines):
    found = 0
    digits = []
    current_num = 0
    bounds = [0, 0]
    for column, letter in enumerate(line):
        if letter.isdigit():
            if not digits:
                bounds[0] = bounds[1] = column
            else:
                bounds[1] = column
            digits.append(letter)

        elif digits:
            # We Completed a num
            # Assemble
            num = 0
            for digit_idx, digit in enumerate(reversed(digits)):
                num += int(digit + "0" * digit_idx)
            print(num, digits, line, bounds)
            digits.clear()
            
            # We need to check the proxim slots
            #       b b
            #   1 2 3 4 5 6 7
            # 1 . . . . . . .
            # 2 . . 4 5 . . .
            # 3 . . . . . . .

            # check before and after
            valid = False
            if bounds[0] != 0:
                valid = check_column(bounds[0] - 1, max(row - 1, 0), min(row + 1, len(lines) - 1))
                # print(valid)
            if not valid and bounds[1] != len(line) - 1:
                valid = check_column(bounds[1] + 1, max(row - 1, 0), min(row + 1, len(lines) - 1))
            
            if valid:
                print("valid by col")
                parts.append(num)
                continue
            
            for col in range(bounds[0], bounds[1] + 1):
                # Check Up and down
                if row != 0:
                    slot = lines[row - 1][col]
                    if slot != "." and not slot.isdigit() and slot != "\n":
                        valid = True
                        break
                if row != len(lines) - 1:
                    slot = lines[row + 1][col]
                    if slot != "." and not slot.isdigit() and slot != "\n":
                        valid = True
                        break
            if valid:
                parts.append(num)
                continue


print(parts, sum(parts), len(set(parts)) == len(parts))



