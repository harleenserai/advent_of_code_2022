from __future__ import annotations
import copy

class File:

    def __init__(self, name, size: int, parent: Directory):
        self.name = name
        self.size = size
        self.parent = parent

    def __eq__(self, other):
        if isinstance(other, File):
            return self.name == other.name and self.size == other.size and self.parent == other.parent
        return False
    
    def getPath(self) -> str:
        return f"{self.parent.getPath()}/{self.name}"

    def __str__(self):
        return f"File(name={self.name})"

class Directory:

    def __init__(self, name, parent: Directory):
        self.name = name
        self.parent = parent
        self.children = []
    
    def addChild(self, child):
        self.children.append(child)
    
    def getPath(self) -> str:
        if self.parent is None:
            return self.name
        
        parent = self.parent.getPath()
        if parent != "/":
            return f"{parent}/{self.name}"
        return f"/{self.name}"

    def getDirectory(self, child_name):
        for content in self.children:
           if isinstance(content, Directory) and content.name == child_name:
                return content
        return None

    def getSize(self) -> int:
        size = 0
        for node in self.children:
            if isinstance(node, File) :
                size += node.size
            elif isinstance(node, Directory):
                size += node.getSize()
        return size
    
    def __eq__(self, other):
        if isinstance(other, Directory):
            return self.name == other.name and self.parent == other.parent
        return False
    
    def __str__(self):
        return f"Directory(name={self.name})"


def main():

    root_directory = parse_file()
    results_store_of_dir_sizes = {}
    calculate_sizes(root_directory, results_store_of_dir_sizes)

    #part 1
    directories_under_100000 = get_dirs_smaller_than_size(100000, results_store_of_dir_sizes)
    print(f"Sum of sizes of directories under 100KB: {sum(directories_under_100000.values())}")

    #part 2
    total_space_of_file_system = 70000000
    space_needed_for_update = 30000000
    available_space = total_space_of_file_system - root_directory.getSize()
    if (space_needed_for_update > available_space):
        additional_space_needed_for_update = space_needed_for_update - available_space
        directories_with_available_space = get_dirs_greater_than_size(additional_space_needed_for_update, results_store_of_dir_sizes)
        sorted_dict = dict(sorted(directories_with_available_space.items(), key=lambda item: item[1]))
        print(f"Top candidate size: {list(sorted_dict.values())[0]}")

def get_dirs_smaller_than_size(required_size, results_store_of_dir_sizes) -> {}:
    results_store_for_dirs_smaller_than_size = {}
    for index, dir in enumerate(results_store_of_dir_sizes):
        dir_size = results_store_of_dir_sizes[dir]
        if (dir_size <= required_size):
            results_store_for_dirs_smaller_than_size[dir] = dir_size
    return results_store_for_dirs_smaller_than_size

def get_dirs_greater_than_size(required_size, results_store_of_dir_sizes) -> {}:
    results_store_for_dirs_smaller_than_size = {}
    for index, dir in enumerate(results_store_of_dir_sizes):
        dir_size = results_store_of_dir_sizes[dir]
        if (dir_size >= required_size):
            results_store_for_dirs_smaller_than_size[dir] = dir_size
    return results_store_for_dirs_smaller_than_size

def calculate_sizes(node: Directory, map: {}):
    if isinstance(node, Directory) == True:
        map[node.getPath()] = int(node.getSize())
        for child in node.children:
            if isinstance(child, Directory) == True:
                calculate_sizes(child, map)

def parse_file() -> Directory:
    file_path = 'advent-day7-2022/2022-puzzle7-input.txt'#test_input.txt'#
   
    root_directory = Directory("/", None)
    with open(file_path, 'r', encoding="utf-8") as file:
         for line_number, line in enumerate(file):
            match line.strip().split():
                case ['$', 'cd', '/']:
                    currentlySelectedNode = root_directory
                case ['$', 'cd', '..']:
                    if currentlySelectedNode.parent:
                        currentlySelectedNode = currentlySelectedNode.parent
                case ['$', 'cd', directory_name]:
                    dir = currentlySelectedNode.getDirectory(directory_name)
                    if dir: 
                        currentlySelectedNode = dir
                case ['$', 'ls']:
                    continue
                case ['dir', directory_name]:
                    currentlySelectedNode.addChild(Directory(directory_name, currentlySelectedNode))
                case [file_size, file_name]:
                    currentlySelectedNode.addChild(File(file_name, int(file_size), currentlySelectedNode))
    return root_directory

if __name__ == "__main__":
    main()
        