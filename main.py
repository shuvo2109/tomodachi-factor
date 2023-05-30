from cards import deck, deck_keys, deck_values
from classes import Player
# from colorama import Style, Fore
from functions import calculate_pause_time_from_list, card_can_be_taken, factors, game_has_to_end,\
    print_formatted_list, refine_input
from time import sleep


def main():
    # Get player name
    player_name = refine_input(prompt='Enter your name: ', type_=str)

    # Set players
    player = Player(name=player_name)
    fate = Player(name='Fate')

    while True:
        print(f"\nYour score: {player.score}\tFate's score: {fate.score}")
        sleep(1)
        print(f"\nYour cards:")
        print_formatted_list(player.cards)
        sleep(1.5)
        print(f"\nFate's cards:")
        print_formatted_list(fate.cards)
        sleep(1.5)
        print(f"\nRemaining cards:")
        print_formatted_list(deck_keys)
        sleep(1.5)
        print("-" * 40)

        # Player takes card
        chosen_card = input("Choose a card: ")
        while True:
            if card_can_be_taken(chosen_card, deck_keys, deck_values, deck):
                break
            chosen_card = input("Invalid choice. Try again. Choose a card: ")

        print("\nYou chose the card:", chosen_card)
        sleep(1)

        # Place card from deck to player
        index = deck_keys.index(chosen_card)
        deck_keys.pop(index)
        deck_values.pop(index)
        player.cards.append(chosen_card)

        # Update player score
        chosen_card_value = deck[chosen_card]
        player.score += chosen_card_value

        # Fate takes cards, place card from table to fate, update fate score
        cards_to_take = []
        chosen_card_factors = factors(chosen_card_value)
        for factor in chosen_card_factors:
            if factor not in deck_values:
                continue
            index = deck_values.index(factor)
            card = deck_keys[index]
            deck_keys.pop(index)
            deck_values.pop(index)
            cards_to_take.append(card)

        print("\nFate chose the cards:", ", ".join(cards_to_take))
        sleep(calculate_pause_time_from_list(cards_to_take))

        for card in cards_to_take:
            fate.cards.append(card)
            fate.score += deck[card]

        # Check if game can continue
        if game_has_to_end(deck_keys, deck_values, deck):
            print("\nThere are no more valid cards for you to take.\n"
                  "Fate takes all the remaining cards.\n")
            for index in range(len(deck_keys) - 1, -1, -1):
                card = deck_keys[index]
                deck_keys.pop(index)
                deck_values.pop(index)
                fate.cards.append(card)
                fate.score += deck[card]

            # Final information display
            print(f"\nYour score: {player.score}\tFate's score: {fate.score}")
            sleep(1)
            print("\nYour cards:")
            print_formatted_list(player.cards)
            sleep(calculate_pause_time_from_list(player.cards))
            print("\nFate's cards:")
            print_formatted_list(fate.cards)
            sleep(calculate_pause_time_from_list(fate.cards))

            # Result declaration
            if player.score > fate.score:
                print("\nCongratulations! You won!")
            elif player.score == fate.score:
                print("\nIt's a tie but as per the rules, Fate wins!")
            elif player.score < fate.score:
                print("\nSorry... you lost!")

            break

    bye = input("Thanks for playing!")


if __name__ == '__main__':
    main()
