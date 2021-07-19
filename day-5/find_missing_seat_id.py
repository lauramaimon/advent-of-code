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


def get_missing_seat_ids(seats: List[str]) -> List[int]:
    missing_seat_ids = list(range(1024))
    for seat in seats:
        seat_id = get_id_of_seat(seat)
        missing_seat_ids.remove(seat_id)
    return missing_seat_ids


def get_missing_seat(seats: List[str]):
    missing_seat_ids = get_missing_seat_ids(seats)

    # the missing seat will be adjacent to two existing seat ids
    for i in range(1, len(missing_seat_ids) - 1):
        if missing_seat_ids[i - 1] < missing_seat_ids[i] - 1:
            if missing_seat_ids[i + 1] > missing_seat_ids[i] + 1:
                return missing_seat_ids[i]

    return None


def get_seats(filepath: str) -> List[str]:
    with open(filepath) as f:
        seats = f.read().splitlines()
    return seats


def get_missing_seat_id(filepath: str) -> int:
    seats = get_seats(filepath)
    return get_missing_seat(seats)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <input file path>')
        sys.exit(1)
    print(f'Missing seat ID: {get_missing_seat_id(sys.argv[1])}')
