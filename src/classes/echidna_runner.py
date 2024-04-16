import subprocess
import time

from loguru import logger


class EchidnaRunner:

    def __init__(self, file_path: str):
        """Initiates the class with the .experiment.sol file passed as argument

        Args:
            file_path (str): solidity file to be run with Echidna
        """
        self.file_path = file_path

    def run_echidna(self):
        """Function to run Echidna, and save output for future analysis"""
        try:
            # Open log file for writing
            with open("echidna_output.log", "a") as output_file:

                echidna_process = subprocess.Popen(
                    ["echidna", "--test-mode", "assertion", self.file_path],
                    stdout=output_file,
                    stderr=subprocess.STDOUT,  # Merge stderr into stdout
                )

                # waiting time for asserts
                time.sleep(10)

                echidna_process.send_signal(subprocess.signal.SIGINT)
                logger.debug("Sent ESC character signal to Echidna process.")

        except subprocess.CalledProcessError as e:
            logger.error(f"Echidna failed with error: {e}")
        except FileNotFoundError:
            logger.error(
                "Echidna executable not found. Please make sure Echidna is installed and added to your PATH."
            )
