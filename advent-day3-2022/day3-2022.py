
def main():
    rumsack = parse_file();
    item_priority_map = {}
    rumsack_elements='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if len(rumsack_elements) == 52:
        for index, char in enumerate(rumsack_elements):
            item_priority_map[char] = index + 1

    priority_sum = 0
    for index, items in enumerate(rumsack):
        compartment_1 = items[0]
        compartment_2 = items[1]
        common_letters = compartment_1 & compartment_2
        if len(common_letters) == 1:
            common_letter = common_letters.pop()
            print(f"Common letter at index {index} is {common_letter}")
            priority_sum += item_priority_map[common_letter]
    
    print(f"The total priority of the mis-packed item is {priority_sum}")
    pass

def parse_file():
    rumsack = []
    file_path = 'advent-day3-2022/2022-puzzle3-input.txt'
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file):
            try:
                midpoint = len(line) // 2
                compartment_1 = line[:midpoint]
                compartment_2 = line[midpoint:]
                #print(f"{compartment_1},{compartment_2}")
                rumsack.append([set(compartment_1), set(compartment_2)]);
            except ValueError as e:
                print (e)
    return rumsack

if __name__ == "__main__":
    main()
    