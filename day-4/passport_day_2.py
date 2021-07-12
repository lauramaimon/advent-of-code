
from field_validator import is_field_valid

class Passport:

    EXPECTED_FIELDS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

    def __init__(self):
        self.fields = {}


    def add_field(self, key: str, value: str):
        if key in self.EXPECTED_FIELDS:
            self.fields[key] = Field(key, value, is_field_valid(key, value))


    def is_valid(self):
        for key in self.EXPECTED_FIELDS:
            if key not in self.fields:
                return False
            elif not self.fields[key].is_valid:
                return False
        return True


    def __str__(self):
        return '|'.join([str(field) for field in self.fields.values()])


class Field:

    def __init__(self, key, value, is_valid):
        self.key = key
        self.value = value
        self.is_valid = is_valid


    def __str__(self):
        return f'{self.key},{self.value},{self.is_valid}'
