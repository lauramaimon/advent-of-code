import sys
from tree_map import TreeMap


def count_trees_for_slope(tree_map, x: int, y: int):
    current_x = x
    current_y = y
    tree_count = 0
    while tree_map.is_within_map(current_y):
        if tree_map.is_tree(current_x, current_y):
            tree_count += 1
        current_x += x
        current_y += y
    return tree_count


def get_tree_map(filepath: str):
    return TreeMap.from_file(filepath)


def main(filepath: str):
    tree_map = get_tree_map(filepath)
    product = 1
    user_input = 'non-blank'
    while user_input:
        user_input = input('Enter slope as \'x y\' (enter to stop): ').split()
        if len(user_input) == 2:
            x = int(user_input[0])
            y = int(user_input[1])
            product *= count_trees_for_slope(tree_map, x, y)
    return product


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <input file path>')
        sys.exit(1)
    print(f'Product of the number of trees encountered for each slope: {main(sys.argv[1])}')
