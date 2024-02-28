import sys
import argparse

sys.path.append("src/classes")

from program_analyzer import ProgramAnalyzer


def main(file_path):
    program_analyzer = ProgramAnalyzer(file_path)
    program_analyzer.analyze()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program Analyzer")
    parser.add_argument(
        "-f", "--file", required=True, help="Path to the input file", type=str
    )
    args = parser.parse_args()
    main(args.file)
