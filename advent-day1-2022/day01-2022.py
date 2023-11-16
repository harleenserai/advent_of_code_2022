
import heapq

file_path = '2022_puzzle_1a_input.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    
    elf_count = 1
    current_elf_calories = 0
    elf_calories_map = {}

    # Read each line in the file
    for line_number, line in enumerate(file):
        # Strip any leading or trailing whitespaces
        line = line.strip()
        if line: 
            try:
                
                current_elf_calories += int(line)
            except ValueError as e:
                print (e)
        else:
            elf_calories_map[elf_count] = current_elf_calories
            #print(f"Elf {elf_count} has {current_elf_calories} Calories");
            elf_count += 1
            current_elf_calories = 0

    elf_with_max_calories = max(elf_calories_map, key=elf_calories_map.get)
    print(f"Elf {elf_with_max_calories} has the maximum {elf_calories_map[elf_with_max_calories]} Calories");

    top3_elves_with_max_calories = heapq.nlargest(3, elf_calories_map, key=elf_calories_map.get)
    print(top3_elves_with_max_calories)
    
    total_calories_top_3_elves = 0
    for elf in top3_elves_with_max_calories:
        total_calories_top_3_elves += elf_calories_map[elf]
        print(f"Elf {elf} has {elf_calories_map[elf]} calories")
    print(f"Total calories carried by top 3 elves is {total_calories_top_3_elves}")