
class TobogganPasswordPolicy:
    def __init__(self, restricted_letter: str, first_position: int, second_position: int):
        self.restricted_letter = restricted_letter
        self.first_position = first_position
        self.second_position = second_position

    def accepts_password(self, password: str) -> bool:
        first_letter_matches = password[self.first_position - 1] == self.restricted_letter
        second_letter_matches = password[self.second_position - 1] == self.restricted_letter
        return first_letter_matches != second_letter_matches
