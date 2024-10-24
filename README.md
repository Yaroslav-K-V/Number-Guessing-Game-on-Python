# Number-Guessing-Game-on-Python

This Python project is a number guessing game where the user tries to guess a randomly generated number within a specified range. The game provides feedback on whether the guess is too high, too low, or correct.   
This project was developed for https://roadmap.sh/projects/number-guessing-game .
---
**Getting Started:**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Yaroslav-K-V/Number-Guessing-Game-on-Python
   
2. **Run the project:**

   ```bash
   python main.py

***
**Features:**

Multiple difficulty levels: Users can choose from easy, medium, hard or unlimited levels, each with a different number of attempts.

User-friendly interface: The game provides clear instructions and feedback to guide the user.

Random number generation: The game generates a random number within the specified range for each round.

Number guessing timer: Using the Python library, the time taken by the user to guess a number is calculated.

Saving records: Using the OS and JSON libraries, the saving of player records is implemented. The text file is created at the first game. As a result of a successful number guess, the user's name, the number of used attempts, and the game time are stored in the file.
The display of these statistics is also implemented.
