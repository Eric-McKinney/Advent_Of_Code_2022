
with open("input.txt", "r") as f:
    input = f.readlines()


def determine_move(opponent_move : str, outcome : str) -> str:
    winning_pairs = {
        "A": "Paper",
        "B": "Scissors",
        "C": "Rock"
    }
    draw_pairs = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors"
    }
    loss_pairs = {
        "A": "Scissors",
        "B": "Rock",
        "C": "Paper"
    }

    if outcome == "X":
        return loss_pairs[opponent_move]
    elif outcome == "Y":
        return draw_pairs[opponent_move]
    else:
        return winning_pairs[opponent_move]



def main():
    points_for_move = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3
    }
    points_for_outcome = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }

    score = 0
    for line in input:
        opponent_move = line[0]
        outcome = line[2]

        score += points_for_outcome[outcome]

        my_move = determine_move(opponent_move, outcome)
        score += points_for_move[my_move]

    print(score)


if __name__ == "__main__":
    main()
