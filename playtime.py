def calculate_sit_outs(num_players):
    if num_players < 6 or num_players > 12:
        raise ValueError("Number of players must be between 6 and 12.")

    total_slots = 36  # 6 matches with 6 slots each
    base_plays = total_slots // num_players
    extra_plays = total_slots % num_players

    plays = [base_plays + 1 if i < extra_plays else base_plays for i in range(num_players)]
    
    # Calculate the number of times each player needs to sit out
    sit_outs = [6 - play for play in plays]

    return sit_outs

def main():
    try:
        num_players = int(input("Enter the number of players (between 6 and 12): "))
        sit_outs = calculate_sit_outs(num_players)
        for i, sit_out in enumerate(sit_outs):
            print(f"Player {i + 1} needs to sit out {sit_out} times.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
