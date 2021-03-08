
class SledPasswordPolicy:
    def __init__(self, restricted_letter: str, lower_bound: int, upper_bound: int):
        self.restricted_letter = restricted_letter
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def accepts_password(self, password: str) -> bool:
        restricted_letter_count = 0
        for letter in password:
            if letter == self.restricted_letter:
                restricted_letter_count += 1
        return self.lower_bound <= restricted_letter_count <= self.upper_bound
