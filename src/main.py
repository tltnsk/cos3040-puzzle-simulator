"""
Project entry point.

Loads puzzles from a JSON file and starts the Escape Room game.
"""

import argparse
import configparser
from pathlib import Path

from utils.puzzle_loader import load_puzzles
from game.escape_room import EscapeRoom


def _load_paths_from_config(config_path):
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
    parser = argparse.ArgumentParser(description="Escape Room puzzle simulator")
    parser.add_argument(
        "--config",
        default="config.ini",
        help="Path to config file (default: config.ini)",
    )
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = Path(__file__).resolve().parent.parent / config_path

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
    game.start_game(results_file_path=str(results_path) if results_path else None)


if __name__ == "__main__":
    main()
