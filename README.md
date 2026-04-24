# Puzzle Simulator - COS3040 Project

This project is a simple puzzle game. The player registers, chooses which puzzles to play (by type or difficulty), and earns points for correct solutions. At the end, results are saved to a JSON file.

## Class Structure

### Game
- `EscapeRoom`: main controller (menu, player registration, puzzle selection, gameplay loop, scoring, saving).

### Player
- `Player`: stores player `name`, `age`, and `score` with validation and helper methods (`add_score`, `reset_score`).

### Puzzles
- `Puzzle`: abstract base class for all puzzles (`id`, `description`, `difficulty`, `max_attempts`, `points`, `attempts_made`, `solved`) and abstract method `check_solution`.
- `TextPuzzle`: abstract base for text answers (`correct_answer`, `allowed_variations`).
  - `GuessWordPuzzle`: guess the missing-letter word. It tracks incorrect guesses.
  - `RiddlePuzzle`: riddle puzzle. It allows hints.
- `MathPuzzle`: abstract base for numeric answers (`correct_result`).
  - `EquationPuzzle`: numeric result with tolerance for floating point comparisons.
  - `LogicPuzzle`: numeric logic question. At the end, it provides an explanation.

### Utilities (File Handling)
- `load_puzzles`: loads puzzle objects from a JSON file.
- `result_manager`: loads, appends and saves results in a JSON file.

## Special Functions / Algorithms Used
- **Operator overloading** in `Puzzle` (`__lt__`, `__eq__`) to compare puzzles (by difficulty / by id).
- **Polymorphism** via `Puzzle.check_solution(...)`: each puzzle type validates answers differently, but `EscapeRoom` calls the same method.
- **Hints** for riddles: `RiddlePuzzle.use_hint()` returns the next hint for the puzzle.
- **Tolerance-based numeric checking**: `EquationPuzzle` uses `math.isclose(...)` to compare float answers.
- **File error handling**: results loading handles missing, empty or invalid JSON.
- **Puzzle Filtering**: the program includes filtering functions so that a player can choose puzzles either by type or by difficulty.


## Project Structure

cos3040-puzzle-simulator/
├── config.ini
├── data/
│   ├── puzzles.json
│   └── results.json
├── src/
│   ├── main.py
│   ├── game/
│   │   └── escape_room.py
│   ├── models/
│   │   ├── player.py
│   │   └── puzzles/
│   │       ├── puzzle.py
│   │       ├── text_puzzle.py
│   │       ├── math_puzzle.py
│   │       ├── guess_word_puzzle.py
│   │       ├── riddle_puzzle.py
│   │       ├── equation_puzzle.py
│   │       └── logic_puzzle.py
│   └── utils/
│       ├── puzzle_loader.py
│       └── result_manager.py
└── tests/


## How to Run

### 1) Configure file paths
This project uses a config file so the file names are not hard-coded in the code.

Edit `config.ini`:
```ini
[DATA]
PATH = data
PUZZLES = puzzles.json
RESULTS = results.json
```

### 2) Start the program
From the project root run:
```bash
python -m src.main
```

### 3) Playing the game
- Use the menu to start.
- When the program starts, the player can:
  - start the game
  - read instructions
  - exit

### 4) Register the player
The program asks the player to enter name and age. After registration, the game begins. 

### 5) Choose puzzles 
The player can choose puzzles:
  - by type
  - by difficulty

Supported puzzle types are:
  - guess word
  - riddle
  - equation
  - logic

### 6) Solve puzzles
The player enters answers directly in the terminal. 
  - text puzzles require a word or phrase
  - math puzzles require a numbers
  - for riddles, the player can type hint to receive a hint

If the answer is correct, the player receives the number of points assigned to that puzzle. 

### 7) Finish the game
At the end of the round, the player can choose to stop the game or play another game.
If the player stops the game, the result is saved to the results file. 

## Data Formats
- Puzzles file: JSON list of puzzle entries.
- Results file: JSON list of result objects.
