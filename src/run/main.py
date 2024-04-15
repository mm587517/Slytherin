import argparse
import sys

from loguru import logger

sys.path.append("src/classes")


from file_modifier import FileModifier
from program_analyzer import ProgramAnalyzer

logger.add("loguru.log")


def main(input_file, output_file):

    program_analyzer = ProgramAnalyzer(input_file)
    program_analyzer.analyze()

    modifier = FileModifier(output_file)
    modifier.find_and_comment()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program Analyzer")
    parser.add_argument(
        "-i", "--input", required=True, help="Path to the input file", type=str
    )
    parser.add_argument(
        "-o", "--output", required=True, help="Path to the output file", type=str
    )
    args = parser.parse_args()
    main(args.input, args.output)
