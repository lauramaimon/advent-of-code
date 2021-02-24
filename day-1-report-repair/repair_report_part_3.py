
import sys
from functools import reduce
from typing import List
from time import time
from repair_report_part_1 import get_entries, sorted_list_contains


def find_n_entries_summing_to_int(n: int, sorted_entries: List[int], target_sum: int) -> tuple:
    if n == 1:
        if sorted_list_contains(sorted_entries, target_sum):
            return (target_sum,)
        else:
            return ()

    for entry in sorted_entries:
        needed_sum = target_sum - entry
        n_minus_1_entries = find_n_entries_summing_to_int(n - 1, sorted_entries, needed_sum)
        if n_minus_1_entries:
            return n_minus_1_entries + (entry,)
    return ()


def main(filepath: str, n: int, target_sum: int) -> int:
    entries = sorted(get_entries(filepath))
    entries = find_n_entries_summing_to_int(n, entries, target_sum)
    if len(entries) != n:
        return None
    print(f'Entries {entries} add to {target_sum}')
    return entries


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f'Usage: {sys.argv[0]} <input file path> <num entries which sum to target> <target sum>')
        sys.exit(1)
    start = time()
    print(f'The answer is {main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))}')
    print(f'Took {time() - start}')
