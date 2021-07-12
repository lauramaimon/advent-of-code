import sys
# from passport_day_1 import Passport
from passport_day_2 import Passport


def count_valid_passports(filepath: str):
    with open(filepath) as f:
        valid_passport_count = 0
        current_passport = Passport()
        for line in f:
            line = line.strip()
            if not line:
                if current_passport.is_valid():
                    valid_passport_count += 1
                current_passport = Passport()
            else:
                for field in line.split(' '):
                    key, value = field.split(':')
                    current_passport.add_field(key, value)
    if current_passport.is_valid():
        valid_passport_count += 1
    return valid_passport_count


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <input file path>')
        sys.exit(1)
    print(f'Number of valid passports: {count_valid_passports(sys.argv[1])}')
