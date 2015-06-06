__author__ = 'lau'

# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
# "ABCDEFGHIJKLMNO" "AGMBFHLNCEIKODJ"
# A     G     M  0
# B   F H   L N  1
# C E   I K   O  2
# D     J        3


def convert(s, num_rows):
    if num_rows == 1:
        return s
    s_list = list(s)
    s_len = len(s_list)
    pat_set = int((s_len + num_rows - 1)/num_rows)
    for add_item in range(len(s_list), pat_set*(2 * num_rows - 2)):
        s_list.append(' ')
    s_lines = []
    for line in range(0, num_rows):
        s_lines.append([])
    for j in range(0, pat_set):
        switch = 0
        row = 0
        for i in range(j * (2 * num_rows - 2), (j + 1)*(2 * num_rows - 2)):
            s_lines[row].append(s_list[i])
            if switch == 1:
                row -= 1
            if switch == 0 and row < num_rows:
                row += 1
                if row == num_rows:
                    switch = 1
                    row -= 2
    new_str = ''
    for row in range(0, num_rows):
        new_str += ''.join(s_lines[row]).replace(' ', '').strip()
    return new_str
