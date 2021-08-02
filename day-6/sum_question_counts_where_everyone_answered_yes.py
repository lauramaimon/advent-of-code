import sys

def get_sum_of_question_counts_where_everyone_answered_yes(filepath: str):
    with open(filepath) as f:
        total_sum = 0
        positive_questions_for_current_group = set()
        first = True
        for line in f:
            line = line.strip()
            if not line:
                total_sum += len(positive_questions_for_current_group)
                positive_questions_for_current_group.clear()
                first = True
                continue 
            if first:
                first = False
                positive_questions_for_current_group.update(letter for letter in line)
            else:
                positive_questions_for_current_group.intersection_update({letter for letter in line})
    return total_sum + len(positive_questions_for_current_group)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <input file path>')
        sys.exit(1)
    print(f'Sum: {get_sum_of_question_counts_where_everyone_answered_yes(sys.argv[1])}')
