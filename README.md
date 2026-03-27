# Puzzle Simulator - COS3040 Project

This project is a simple puzzle game. The player registers, chooses which puzzles to play (by type or difficulty), and earns points for correct solutions. At the end, results can be saved to a JSON file.

## Class Structure

### Game
- `EscapeRoom`: main controller (menu, player registration, puzzle selection, gameplay loop, scoring, saving).

### Player
- `Player`: stores `id`, `name`, `age`, and `score` with validation and helper methods (`add_score`, `reset_score`).

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
From the project root:
```bash
PYTHONPATH=src python3 src/main.py
```

Optional (use a different config):
```bash
PYTHONPATH=src python3 src/main.py --config other.ini
```

### 3) Playing the game
- Use the menu to start.
- Choose puzzles by type or difficulty.
- For riddles you can type `hint` to reveal the next hint.

## Data Formats
- Puzzles file: JSON list of puzzle entries.
- Results file: JSON list of result objects.
