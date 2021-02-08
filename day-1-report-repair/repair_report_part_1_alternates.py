
from typing import List

def binary_search_contains_v1(sorted_entries: List[int], target_int: int):
    length = len(sorted_entries)
    if length == 0:
        return False
    elif length == 1:
        return sorted_entries[0] == target_int
    
    mid = length // 2
    if sorted_entries[mid] > target_int:
        return binary_search_contains_v1(sorted_entries[0:mid], target_int)
    elif sorted_entries[mid] < target_int:
        return binary_search_contains_v1(sorted_entries[mid:-1], target_int)
    else:
        return True


def find_entries_summing_to_int_in(entries: List[int], target_sum: int):
    sorted_entries = sorted(entries)
    for entry in sorted_entries:
        needed_entry = target_sum - entry
        if needed_entry in entries:
            return entry, needed_entry


def find_entries_summing_to_int_sorted(entries: List[int], target_sum: int):
    sorted_entries = sorted(entries)
    reversed_entries = reversed(sorted_entries)
    for entry in sorted_entries:
        for other_entry in reversed_entries:
            if entry + other_entry < target_sum:
                break
            elif entry + other_entry == target_sum:
                return entry, other_entry


def find_entries_summing_to_int_unoptimized(entries: List[int], target_sum: int):
    for entry in entries:
        for other_entry in entries:
            if entry + other_entry == target_sum:
                return entry, other_entry
