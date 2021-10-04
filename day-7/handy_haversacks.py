
import sys
import re

BAG_RULE_REGEX = re.compile(r'^([\w\s]+) bags contain (.*)\n?$')
INNER_BAG_REGEX = re.compile(r'(\d+) ([\w\s]+) bags?(?:, |.)')


def read_rules(filepath: str) -> dict:
    rules = {}
    with open(filepath) as f:
        for line in f:
            match = BAG_RULE_REGEX.fullmatch(line)
            if match is None:
                raise Exception(f'Line did not match regex: {line}')

            color = match.group(1)
            rules[color] = {}
            inner_bags = match.group(2)
            inner_bag_matches = INNER_BAG_REGEX.findall(inner_bags)
            for match in inner_bag_matches:
                inner_color = match[1]
                inner_color_count = int(match[0])
                rules[color][inner_color] = inner_color_count
    return rules


def can_bag_color_contain_target_color(rules: dict, memoized_results: dict, bag_color: str, target_color: str) -> bool:
    if bag_color in memoized_results:
        return memoized_results[bag_color]

    inner_bags = rules[bag_color]
    if len(inner_bags) == 0:
        memoized_results[bag_color] = False
        return memoized_results[bag_color]

    if target_color in inner_bags:
        memoized_results[bag_color] = True
        return memoized_results[bag_color]

    for inner_bag in inner_bags:
        if inner_bag in memoized_results and memoized_results[inner_bag]:
            memoized_results[bag_color] = True
            return memoized_results[bag_color]

        elif can_bag_color_contain_target_color(rules, memoized_results, inner_bag, target_color):
            memoized_results[bag_color] = True
            return memoized_results[bag_color]

    memoized_results[bag_color] = False
    return memoized_results[bag_color]


def count_bag_colors_that_contain_target_color(rules: dict, target_color: str) -> int:
    memoized_results = {}
    num_bags_containing_gold = 0
    for bag in rules:
        if can_bag_color_contain_target_color(rules, memoized_results, bag, target_color):
            num_bags_containing_gold += 1
    return num_bags_containing_gold


def count_bags_required_inside_bag_color_inner(memoized_bag_counts: dict, rules: dict, bag_color: str) -> int:
    if bag_color in memoized_bag_counts:
        return memoized_bag_counts[bag_color]

    count = 0
    requirements = rules[bag_color]
    for inner_bag in requirements:
        number_of_inner_bag = requirements[inner_bag]
        number_of_bags_in_inner_bag = count_bags_required_inside_bag_color_inner(memoized_bag_counts, rules, inner_bag)
        count += number_of_inner_bag * (1 + number_of_bags_in_inner_bag)

    memoized_bag_counts[bag_color] = count
    return count


def count_bags_required_inside_bag_color(rules: dict, target_color: str) -> int:
    memoized_bag_counts = {}
    return count_bags_required_inside_bag_color_inner(memoized_bag_counts, rules, target_color)


def main(filepath: str) -> int:
    rules = read_rules(filepath)
    target_color = "shiny gold"

    # part 1
    bags_containing_gold = count_bag_colors_that_contain_target_color(rules, target_color)
    print(f'Bag colors can eventually contain at least one shiny gold bag: {bags_containing_gold}')

    # part 2
    total_bags_within_gold_bag = count_bags_required_inside_bag_color(rules, target_color)
    print(f'Number of individual bags that are required inside a single shiny gold bag: {total_bags_within_gold_bag}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <input file path>')
        sys.exit(1)
    main(sys.argv[1])
