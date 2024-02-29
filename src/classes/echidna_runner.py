import subprocess
from loguru import logger
import time


class EchidnaRunner:
    def __init__(self, file_path):
        self.file_path = file_path

    def run_echidna(self):
        try:
            # Open log file for writing
            with open("echidna_output.log", "a") as output_file:

                echidna_process = subprocess.Popen(
                    ["echidna", "--test-mode", "assertion", self.file_path],
                    stdout=output_file,
                    stderr=subprocess.STDOUT,  # Merge stderr into stdout
                )

                time.sleep(10)

                echidna_process.send_signal(subprocess.signal.SIGINT)
                logger.info("Sent ESC character signal to Echidna process.")

        except subprocess.CalledProcessError as e:
            logger.error(f"Echidna failed with error: {e}")
        except FileNotFoundError:
            logger.error(
                "Echidna executable not found. Please make sure Echidna is installed and added to your PATH."
            )
