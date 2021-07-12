import re


def is_field_valid(key: str, value: str):
    if key == 'byr':
        return is_byr_valid(value)
    elif key == 'iyr':
        return is_iyr_valid(value)
    elif key == 'eyr':
        return is_eyr_valid(value)
    elif key == 'hgt':
        return is_hgt_valid(value)
    elif key == 'hcl':
        return is_hcl_valid(value)
    elif key == 'ecl':
        return is_ecl_valid(value)
    elif key == 'pid':
        return is_pid_valid(value)
    return True


def is_pid_valid(pid: str):
    pattern = re.compile(r'\d{9}')
    if pattern.fullmatch(pid):
        return True
    return False


def is_ecl_valid(color: str):
    return color in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def is_hcl_valid(color: str):
    pattern = re.compile(r'#[0-9a-f]{6}')
    if pattern.fullmatch(color):
        return True
    return False


def is_hgt_valid(height: str):
    pattern = re.compile(r'(\d{2,3})(cm|in)')
    match = pattern.fullmatch(height)
    if not match:
        return False

    num = int(match.group(1))
    unit = match.group(2)
    if unit == 'cm':
        return 150 <= num <= 193
    elif unit == 'in':
        return 59 <= num <= 76


def is_byr_valid(year: str):
    return is_year_in_range(year, 1920, 2002)


def is_iyr_valid(year: str):
    return is_year_in_range(year, 2010, 2020)


def is_eyr_valid(year: str):
    return is_year_in_range(year, 2020, 2030)


def is_year_in_range(year: str, minimum: int, maximum: int):
    try:
        integer_year = int(year)
        return minimum <= integer_year <= maximum
    except ValueError:
        return False
