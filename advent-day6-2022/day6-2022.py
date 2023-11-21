
from collections import defaultdict
import copy

def main():
    transmission_start_index = parse_file(4)
    print(f"transmission start index for marker size 4: {transmission_start_index}")

    transmission_start_index = parse_file(14)
    print(f"transmission start index for marker size 14: {transmission_start_index}")

def parse_file(marker_size) -> int:
    file_path = 'advent-day6-2022/2022-puzzle6-input.txt'
   
    with open(file_path, 'r', encoding="utf-8") as file:
        buffer_index = marker_size
        buffer_size = marker_size
        file.seek(buffer_index-buffer_size)
        buffer = file.read(buffer_size)
        while (buffer):
            print(f"buffer: {tuple(buffer)}, set buffer: {tuple(set(buffer))}")
            if (len(tuple(buffer)) == len(tuple(set(buffer)))):
                print("no duplicates in buffer")
                return buffer_index
            buffer_index += 1
            file.seek(buffer_index-buffer_size)
            buffer = file.read(buffer_size)
            
        

if __name__ == "__main__":
    main()