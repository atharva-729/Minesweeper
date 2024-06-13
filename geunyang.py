import tkinter as tk

def create_difficulty_window():
    # Create a new window for the difficulty selection
    difficulty_window = tk.Tk()
    difficulty_window.title("Choose Difficulty")
    difficulty_window.geometry("350x450")
    difficulty_window.config(bg="lightgreen")

    # Define functions for button clicks
    def choose_easy():
        start_button.destroy()  # Close the difficulty window
        difficulty_window.destroy()

    def choose_medium():
        difficulty_window.destroy()
        start_button.destroy()

    def choose_hard():
        difficulty_window.destroy()
        start_button.destroy()

    # Create buttons for each difficulty
    font1=("Arial", 14, "bold")
    easy_button = tk.Button(difficulty_window, text="not so easy", command=choose_easy, bg="white", font=font1)
    medium_button = tk.Button(difficulty_window, text="kinda hard", command=choose_medium, bg="skyblue", font=font1)
    hard_button = tk.Button(difficulty_window, text="PRESS TO DIE", command=choose_hard, bg="red", font=font1)

    # Arrange buttons in the window
    easy_button.grid(row=0, column=0, padx=100, pady=50)
    medium_button.grid(row=1, column=0, padx=100, pady=50)
    hard_button.grid(row=2, column=0, padx=100, pady=50)

    # Run the event loop for the difficulty window
    difficulty_window.mainloop()

# Create the main game window (after defining functions)

root = tk.Tk()
root.title("Minesweeper")
root.geometry("100x100")

# Button to launch the difficulty selection window
start_button = tk.Button(root, text="Start Game", command=create_difficulty_window)
start_button.pack()

# Run the event loop for the main window (after the difficulty window)
root.mainloop()
