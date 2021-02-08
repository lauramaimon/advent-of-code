
import sys
from typing import List
from time import time


def binary_search_contains(sorted_entries: List[int], begin_index: int, end_index: int, target_int: int):
    if begin_index == end_index:
        return sorted_entries[begin_index] == target_int
    elif begin_index > end_index:
        return False
    
    mid = begin_index + ((end_index - begin_index) // 2)
    if sorted_entries[mid] > target_int:
        return binary_search_contains(sorted_entries, begin_index, mid, target_int)
    elif sorted_entries[mid] < target_int:
        return binary_search_contains(sorted_entries, mid + 1, end_index, target_int)
    else:
        return True


def sorted_list_contains(sorted_entries: List[int], target: int):
    return binary_search_contains(sorted_entries, 0, len(sorted_entries), target)


def find_two_entries_summing_to_int(sorted_entries: List[int], target_sum: int):
    for entry in sorted_entries:
        needed_entry = target_sum - entry
        if sorted_list_contains(sorted_entries, needed_entry):
            return entry, needed_entry


def get_entries(filepath: str) -> List[int]:
    entries = []
    with open(filepath) as f:
        entries = [int(entry) for entry in f.read().split()]
    return entries
    

def main(filepath: str):
    target_sum = 2020
    entries = sorted(get_entries(filepath))
    first, second = find_two_entries_summing_to_int(entries, target_sum)
    print(f'Entries {first} and {second} add to {target_sum}')
    return first * second


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <input file path>')
        sys.exit(1)
    start = time()
    print(f'The answer is {main(sys.argv[1])}')
    print(f'Took {time() - start}')