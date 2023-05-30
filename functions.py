from cards import deck_keys
from math import sqrt
from time import sleep


def print_formatted_list(my_list: list,
                         elements_per_line: int = 5,
                         max_length: int = max(len(str(element)) for element in deck_keys)):
    indentation = max_length + 2

    for i, element in enumerate(my_list, start=1):
        if i != 1 and (i - 1) % elements_per_line == 0:
            print()  # Start a new line
        print("{:<{}}".format(element, indentation), end="")

    print()  # Print a newline after the last line


def refine_input(prompt='', type_=None, min_=None, max_=None, range_=None):
    str_not_valid_input = "That is not a valid input. "
    while True:
        if min_ is not None and max_ is not None and max_ < min_:
            raise ValueError("Lower bound must be less than or equal to upper bound.")
        while True:
            variable = input(prompt)
            if type_ is not None:
                try:
                    variable = type_(variable)
                except ValueError:
                    print(str_not_valid_input + "Value has to be {}.".format(type_.__name__))
                    continue
            if max_ is not None and variable > max_:
                print(str_not_valid_input + "Value must be less than or equal to {}.".format(max_))
            elif min_ is not None and variable < min_:
                print(str_not_valid_input + "Value must be greater than or equal to {}".format(min_))
            elif range_ is not None and variable not in range_:
                if isinstance(range_, range):
                    str_must_be_between = "Value must be between {} and {}.".format(range_.start, range_.stop)
                    print(str_must_be_between)
                else:
                    str_var_must_be = "Value must be {}."
                    if len(range_) == 1:
                        print(str_var_must_be.format(*range_))
                    else:
                        expected = " or ".join((", ".join(str(x) for x in range_[:-1]), str(range_[-1])))
                        print(str_var_must_be.format(expected))
            else:
                return variable


def factors(number: int) -> list:
    list_of_factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            list_of_factors.append(i)
    return list_of_factors


def count_remaining_factors(chosen_card: str, deck_values: list, deck: dict) -> int:
    card_factors = factors(deck[chosen_card])
    deck_values_set = set(deck_values)
    remaining_factors = sum(1 for factor in card_factors if factor in deck_values_set)
    return remaining_factors


def card_can_be_taken(chosen_card: str, deck_keys: list, deck_values: list, deck: dict) -> bool:
    if chosen_card not in deck_keys:
        return False
    count = count_remaining_factors(chosen_card, deck_values, deck)
    if count <= 1:
        return False
    return True


def game_has_to_end(deck_keys: list, deck_values: list, deck: dict) -> bool:
    if len(deck_keys) == 0:
        return True

    for card in deck_keys:
        if card_can_be_taken(card, deck_keys, deck_values, deck):
            return False
    return True


def print_text_with_pause(text, pause_time):
    print(text)  # Display the text
    sleep(pause_time)  # Pause for the specified time


def calculate_pause_time_from_list(cards_to_take: list) -> int:
    pause_time = int(sqrt(len(cards_to_take)))
    if pause_time < 1:
        return 1
    return pause_time
