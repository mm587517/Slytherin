import sys
import argparse
import subprocess
from loguru import logger

sys.path.append("src/classes")

from program_analyzer import ProgramAnalyzer
from echidna_runner import EchidnaRunner


logger.add("loguru.log")


def find_assert_slytherin(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                if "assert" in line and "slytherin" in line:
                    print(line.strip())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


def main(file_path):
    program_analyzer = ProgramAnalyzer(file_path)
    program_analyzer.analyze()

    # echidna = EchidnaRunner(file_path="output/test.experiment.sol")
    # echidna.run_echidna()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program Analyzer")
    parser.add_argument(
        "-f", "--file", required=True, help="Path to the input file", type=str
    )
    args = parser.parse_args()
    main(args.file)
