import re
import sys
from time import time
from typing import List
from sled_password_policy import SledPasswordPolicy
from toboggan_password_policy import TobogganPasswordPolicy


def parse_policy_and_password(password: str, policy_class):
    line_regex = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')
    match = line_regex.fullmatch(password)
    if match is None:
        print(f'Bad line format: "{password}"')
        return None, None

    first_int = int(match.group(1))
    second_int = int(match.group(2))
    restricted_letter = match.group(3)
    policy = policy_class(restricted_letter, first_int, second_int)
    password = match.group(4)
    return policy, password


def count_valid_passwords(filepath: str, policy_class) -> int:
    num_valid = 0
    with open(filepath) as f:
        for line in f:
            policy, password = parse_policy_and_password(line.strip(), policy_class)
            if policy and password:
                if policy.accepts_password(password):
                    num_valid += 1
    return num_valid


def main(filepath: str, policy_type: str) -> int:
    policy_class = SledPasswordPolicy if policy_type == 'sled' else TobogganPasswordPolicy
    return count_valid_passwords(filepath, policy_class)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} <input file path> <sled/toboggan>')
        sys.exit(1)
    start = time()
    print(f'Number of valid passwords: {main(sys.argv[1], sys.argv[2])}')
    print(f'Took {time() - start}')
