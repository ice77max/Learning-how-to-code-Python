import tkinter as tk
import random

# Game logic
moves = ["rock", "paper", "scissors"]
player_score = 0
ai_score = 0

def play(player_move):
    global player_score, ai_score
    ai_move = random.choice(moves)
    result = ""

    if player_move == ai_move:
        result = "It's a draw!"
    elif (player_move == "rock" and ai_move == "scissors") or \
         (player_move == "paper" and ai_move == "rock") or \
         (player_move == "scissors" and ai_move == "paper"):
        result = "You win this round!"
        player_score += 1
    else:
        result = "AI wins this round!"
        ai_score += 1

    result_label.config(text=f"You chose {player_move}, AI chose {ai_move}.\n{result}")
    score_label.config(text=f"Score - You: {player_score} | AI: {ai_score}")

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")

tk.Label(root, text="Choose your move:").pack()

for move in moves:
    tk.Button(root, text=move.title(), width=15, command=lambda m=move: play(m)).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0 | AI: 0", font=("Arial", 12, "bold"))
score_label.pack(pady=10)

root.mainloop()