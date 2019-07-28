player1_input = input("Player1, please enter your choice:")
player2_input = input("Player2, please enter your choice:")

if player1_input == "Rock" and player2_input == "Scissor":
    print("Player1 Wins: Do you want to start a new game?")
if player2_input == "Rock" and player1_input == "Scissor":
    print("Player2 Wins: Do you want to start a new game?")
if player1_input == "Scissor" and player2_input == "Paper":
    print("Player1 Wins: Do you want to start a new game?")
if player2_input == "Scissor" and player1_input == "Paper":
    print("Player2 Wins: Do you want to start a new game?")
if player1_input == "Paper" and player2_input == "Rock":
    print("Player1 Wins: Do you want to start a new game?")
if player2_input == "Paper" and player1_input == "Rock":
    print("Player2 Wins: Do you want to start a new game?")