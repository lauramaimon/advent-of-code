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


def main(filepath: str, x: int, y: int):
    tree_map = get_tree_map(filepath)
    return count_trees_for_slope(tree_map, x, y)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f'Usage: {sys.argv[0]} <input file path> <x> <y>')
        sys.exit(1)
    print(f'Number of trees encountered: {main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))}')
