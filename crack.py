def crack(items, target):
    items_length = len(items)
    combos = []
    valid_combos = []
    number_of_valid = 0
    def gen(combo, depth): # generate combinations
        if depth == 0:
            combos.append(combo)
            return
        gen(combo + '0', depth - 1)
        gen(combo + '1', depth - 1)
    gen('', items_length)
    # test combinations
    for combo in combos:
        total = 0
        temp_list = []
        for index in range(items_length):
            if combo[index] == '1':
                total += items[index]
                temp_list.append(items[index])
        if total == target:
            valid_combos.append(temp_list)
            number_of_valid += 1
    return valid_combos, number_of_valid

print(crack([1,2,3,4,5], 6))
second = [2, 3, 6, 8, 13, 21, 27, 33, 34, 35, 36, 41, 43, 50, 52, 55, 65, 68, 70, 71, 93, 96, 100, 102, 106, 109, 113, 114, 121, 123, 127, 135, 141, 145, 151, 154, 155, 158, 160, 164, 168, 169, 173, 174, 177, 180, 182, 193, 199, 200]
print(len(second))
