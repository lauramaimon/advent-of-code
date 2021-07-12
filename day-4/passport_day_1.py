
class Passport:
    EXPECTED_FIELDS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

    def __init__(self):
        self.fields = []

    def add_field(self, key: str):
        if key in self.EXPECTED_FIELDS:
            self.fields.append(key)

    def is_valid(self):
        for key in self.EXPECTED_FIELDS:
            if key not in self.fields:
                return False
        return True

    def __str__(self):
        return ' '.join([key for key in self.fields])



