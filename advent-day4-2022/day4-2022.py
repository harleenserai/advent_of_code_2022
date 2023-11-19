
def main():
    total_pairs_that_pass_containment_test = 0
    total_pairs_that_pass_overlap_test = 0
    assignment_sections = parse_file()
    for index, assignments in enumerate(assignment_sections):
        if len(assignments) == 2:
            if is_range_between(assignments[0], assignments[1]):
                total_pairs_that_pass_containment_test += 1

            if is_range_overlap(assignments[0], assignments[1]):
                total_pairs_that_pass_overlap_test += 1
            
    print(f"Assignment pairs that contain the other's range fully {total_pairs_that_pass_containment_test}")
    print(f"Assignment pairs that overlap {total_pairs_that_pass_overlap_test}")

def is_range_between(range1, range2):
    start1, end1 = range1
    start2, end2 = range2
    return (start2 <= start1 <= end1 <= end2) or (start1 <= start2 <= end2 <= end1)

def is_range_overlap_2(range1, range2):
    start1, end1 = range1
    start2, end2 = range2
    return (start2 <= start1 <= end2) or (start2 <= end1 <= end2) or (start1 <= start2 <= end1) or (start1 <= end2 <= end1)

def is_range_overlap(range1, range2):
    print(f'ranges {range1}, {range2}')
    start1, end1 = range1
    set1 = set(range(start1, end1+1))
    print(f'set 1 look like {set1}')

    start2, end2 = range2
    set2 = set(range(start2, end2+1))
    print(f'set 2 look like {set2}')
    
    #if len(set1 & set2) > 0:
    print(f'{set1 & set2}')
    return len(set1 & set2) > 0

def parse_file():
    tuples = []
    file_path = 'advent-day4-2022/2022-puzzle4-input.txt'
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file):
            try:
                ranges = line.strip().split(',')
                range_tuples = []
                for index, value in enumerate(ranges):
                    range_tuples.append(tuple(map(int, value.strip().split('-'))))
                tuples.append(tuple(range_tuples))
            except ValueError as e:
                print (e)
    #print(f"{len(tuples)}")
    return tuples

if __name__ == "__main__":
    main()