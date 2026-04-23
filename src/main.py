"""
Project entry point for the puzzle simulator.

Reads file paths from the configuration, loads puzzle definitions, and starts
the Escape Room gameplay.
"""

import configparser
from pathlib import Path
from src.game.escape_room import EscapeRoom
from src.utils.puzzle_loader import load_puzzles


def _load_paths_from_config(config_path):
    """
    Read the configured file locations from the config file.

    Parameters
    ----------
    config_path : Path
        Path to the configuration file.

    Returns
    -------
    tuple
        The puzzles path, results path, and data directory.
    """
    cfile = configparser.ConfigParser()
    read_files = cfile.read(str(config_path))
    if not read_files:
        raise FileNotFoundError(f"Config file not found: {config_path}")

    data_dir = Path(__file__).resolve().parent.parent / cfile["DATA"]["PATH"]
    puzzles_path = data_dir / cfile["DATA"]["PUZZLES"]
    results_name = cfile["DATA"].get("RESULTS", "").strip()
    results_path = (data_dir / results_name) if results_name else None
    return puzzles_path, results_path, data_dir


def main():
    """Load the config, puzzles, and start the game."""
    config_path = Path(__file__).resolve().parent.parent / "config.ini"

    try:
        puzzles_path, results_path, data_dir = _load_paths_from_config(config_path)
    except (FileNotFoundError, KeyError) as exc:
        print(f"Config error: {exc}")
        return

    if not data_dir.exists():
        print(f"Data folder not found: {data_dir}")
        return

    # Show which files are in the data folder.
    for path in data_dir.iterdir():
        print(path)

    try:
        puzzles = load_puzzles(str(puzzles_path))
    except (OSError, ValueError, KeyError) as exc:
        print(f"Could not load puzzles from '{puzzles_path}': {exc}")
        return

    game = EscapeRoom(puzzles)
    try:
        game.start_game(results_file_path=str(results_path) if results_path else None)
    except KeyboardInterrupt:
        print("\nGame interrupted by user.")
        return


if __name__ == "__main__":
    main()
