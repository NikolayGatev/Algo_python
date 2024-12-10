def cer(enter, idx):
    if enter[idx].isdigit():
        return enter[idx]
    if enter[idx] == 't':
        return cer(enter, idx + 2)

    cursor = idx + 2
    conditional_statements_counter = 0
    while True:
        symbol = enter[cursor]
        if symbol == '?':
            conditional_statements_counter += 1
        elif symbol == ':':
            if conditional_statements_counter == 0:
                return enter[cursor + 1]
            else:
                conditional_statements_counter -= 1
        cursor += 1

enter = input().split()
print(cer(enter, 0))