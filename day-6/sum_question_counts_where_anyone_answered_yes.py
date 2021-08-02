import sys


def get_sum_of_question_counts_where_anyone_answered_yes(filepath: str):
    with open(filepath) as f:
        total_sum = 0
        positive_questions_for_current_group = set()
        for line in f:
            line = line.strip()
            if not line:
                total_sum += len(positive_questions_for_current_group)
                positive_questions_for_current_group.clear()
                continue
            
            for letter in line:
                positive_questions_for_current_group.add(letter)
    return total_sum + len(positive_questions_for_current_group)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <input file path>')
        sys.exit(1)
    print(f'Sum: {get_sum_of_question_counts_where_anyone_answered_yes(sys.argv[1])}')
