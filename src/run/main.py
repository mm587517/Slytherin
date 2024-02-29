import sys
import argparse
import subprocess
from loguru import logger

sys.path.append("src/classes")

from program_analyzer import ProgramAnalyzer
from echidna_runner import EchidnaRunner


logger.add("loguru.log")


def main(file_path):
    program_analyzer = ProgramAnalyzer(file_path)
    program_analyzer.analyze()

    echidna = EchidnaRunner(file_path="output/test.experiment.sol")
    echidna.run_echidna()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program Analyzer")
    parser.add_argument(
        "-f", "--file", required=True, help="Path to the input file", type=str
    )
    args = parser.parse_args()
    main(args.file)

# import subprocess
# from loguru import logger
# import threading
# import time

# file_path = "output/test.experiment.sol"
# logger.add("loguru.log")


# def run_echidna(file_path):
#     try:
#         # Open log file for writing
#         with open("echidna_output.log", "w") as output_file:
#             # Run Echidna command with --test-mode assertion flag, redirecting output to file
#             echidna_process = subprocess.Popen(
#                 ["echidna", "--test-mode", "assertion", file_path],
#                 stdout=output_file,
#                 stderr=subprocess.STDOUT,  # Merge stderr into stdout
#             )

#             # Wait for 10 seconds
#             time.sleep(10)

#             # Send the ESC character signal to the process
#             echidna_process.send_signal(subprocess.signal.SIGINT)
#             logger.info("Sent ESC character signal to Echidna process.")

#     except subprocess.CalledProcessError as e:
#         logger.error(f"Echidna failed with error: {e}")
#     except FileNotFoundError:
#         logger.error(
#             "Echidna executable not found. Please make sure Echidna is installed and added to your PATH."
#         )


# # Run Echidna in a separate thread
# echidna_thread = threading.Thread(target=run_echidna, args=(file_path,))
# echidna_thread.start()

# # Wait for the thread to finish
# echidna_thread.join()


# assert\s*\(\s*{([^{}]+)}\s*<=\s*type\(\s*{([^{}]+)}\)\.max\s*{([^{}]+)}\s*{([^{}]+)}\s*{([^{}]+)}\s*\);\s*#slytherin
