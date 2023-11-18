
def main():
    rumsacks = parse_file();
    item_priority_map = {}
    rumsack_elements='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if len(rumsack_elements) == 52:
        for index, char in enumerate(rumsack_elements):
            item_priority_map[char] = index + 1

    priority_sum = 0
    elf_group_size = 3
    elf_counter = 0
    for i in range(0, len(rumsacks), elf_group_size):
       
        sack_1 = set(rumsacks[i])
        sack_2 = set(rumsacks[i+1])
        sack_3 = set(rumsacks[i+2])
       
        common_letters = sack_1 & sack_2 & sack_3
        if len(common_letters) == 1:
            common_letter = common_letters.pop()
            print(f"Common letter at index {index} is {common_letter}")
            priority_sum += item_priority_map[common_letter]
    
    print(f"The badge priority is {priority_sum}")
    pass

def parse_file():
    rumsacks = []
    file_path = 'advent-day3-2022/2022-puzzle3-input.txt'
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file):
            try:
                rumsacks.append(line.strip())
            except ValueError as e:
                print (e)
    return rumsacks

if __name__ == "__main__":
    main()
    