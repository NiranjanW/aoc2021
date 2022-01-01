import random

SUITS = "\u2663  \u2660 \u2666 \u2665".split()
RANK = "2 3 4 55 6 7 8 9 10 J Q K A".split()

# for suite in SUITS:
#     print(suite)


def create_deck(shuffle=False):

    deck = [(i, j) for i in SUITS for j in RANK]
    if shuffle:
        random.shuffle(deck)
    return deck


def deal_hands(deck):
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])


def choose(items):
    return random.choice(items)


def player_order(names, start=None):
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx] + names[:start_idx]


def play():
    """Play a 4-player card game"""
    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)

    # Randomly play cards from each player's hand until empty
    while hands[start_player]:
        for name in turn_order:
            card = choose(hands[name])
            hands[name].remove(card)
            print(f"{name}: {card[0] + card[1]:<3}  ", end="")
        print()

    # for name, cards in hands.items():
    #     card_str = " ".join(f"{s}{r}" for (s, r) in cards)
    #     print(f"{name}: {card_str}")


if __name__ == '__main__':
    play()
