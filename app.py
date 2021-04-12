TARGET_TXT = "target.txt"
OUTPUT_TXT = "output.txt"
HORIZ_ALIGN = ["left", "center", "right"]

print("Horizontal alignment")
for index, mode in enumerate(HORIZ_ALIGN, start=1):
    print(index, ": ", mode, sep="")
SEL_HORIZ_ALIGN = int(input("Selection: "))

with open(TARGET_TXT) as f:
    lines = [line.strip('\n').split(',') for line in f.readlines()]

max_col_widths = [max([len(row) for row in col]) for col in zip(*lines)]
horiz_border_top = '_'*(sum(max_col_widths)+len(max_col_widths)+1) + '\n'
horiz_border_else = '-'*(sum(max_col_widths)+len(max_col_widths)+1) + '\n'

table_rows = [horiz_border_top]
for row in lines:
    new_row = ['|']
    for index, col in enumerate(row):
        if SEL_HORIZ_ALIGN == 1:
            cell = col + ' '*(max_col_widths[index]-len(col)) + '|'
        elif SEL_HORIZ_ALIGN == 2:
            num_of_left_spaces = int((max_col_widths[index]-len(col))/2)
            num_of_right_spaces = max_col_widths[index] - num_of_left_spaces - len(col)
            cell = ' '*num_of_left_spaces + col + ' '*num_of_right_spaces + '|'
        elif SEL_HORIZ_ALIGN == 3:
            cell = ' '*(max_col_widths[index]-len(col)) + col + '|'
        new_row.append(cell)
    new_row.append('\n')
    table_rows.append(new_row)
    table_rows.append(horiz_border_else)

with open(OUTPUT_TXT, "a") as f:
    f.truncate(0)
    for row in table_rows:
        for col in row:
            f.write(col)
