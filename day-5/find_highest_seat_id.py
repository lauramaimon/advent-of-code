import sys
from typing import List


def get_row_of_seat(seat: str):
    row = 0
    for i in range(0, 7):
        if seat[i] == 'B':
            row += 2 ** (6 - i)
    return row


def get_column_of_seat(seat: str):
    column = 0
    for i in range(7, 10):
        if seat[i] == 'R':
            column += 2 ** (9 - i)
    return column


def get_id_of_seat(seat: str) -> int:
    row = get_row_of_seat(seat)
    column = get_column_of_seat(seat)
    return row * 8 + column


def get_seat_ids(seats: List[str]) -> List[int]:
    seat_ids = []
    for seat in seats:
        seat_ids.append(get_id_of_seat(seat))
    return seat_ids


def get_seats(filepath: str) -> List[str]:
    with open(filepath) as f:
        seats = f.read().splitlines()
    return seats


def get_highest_seat_id(filepath: str) -> int:
    seats = get_seats(filepath)
    return max(get_seat_ids(seats))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <input file path>')
        sys.exit(1)
    print(f'Highest seat ID: {get_highest_seat_id(sys.argv[1])}')
