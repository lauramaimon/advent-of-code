
import sys
from typing import List
from time import time
from repair_report_part_1 import get_entries, sorted_list_contains, binary_search_contains


def find_two_entries_summing_to_int(sorted_entries: List[int], target_sum: int):
    for entry in sorted_entries:
        needed_entry = target_sum - entry
        if sorted_list_contains(sorted_entries, needed_entry):
            return entry, needed_entry
    return None, None


def find_three_entries_summing_to_int(sorted_entries: List[int], target_sum: int):
    for entry in sorted_entries:
        needed_sum = target_sum - entry
        second, third = find_two_entries_summing_to_int(sorted_entries, needed_sum)
        if second and third:
            return entry, second, third
    return None, None, None
    

def main(filepath: str):
    target_sum = 2020
    entries = sorted(get_entries(filepath))
    first, second, third = find_three_entries_summing_to_int(entries, target_sum)
    if not (first and second and third):
        return None
    print(f'Entries {first} and {second} and {third} add to {target_sum}')
    return first * second * third


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <input file path>')
        sys.exit(1)
    start = time()
    print(f'The answer is {main(sys.argv[1])}')
    print(f'Took {time() - start}')