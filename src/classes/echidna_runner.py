import subprocess
from loguru import logger
import threading
import time


class EchidnaRunner:
    def __init__(self, file_path):
        self.file_path = file_path

    def run_echidna(self):
        try:
            # Open log file for writing
            with open("echidna_output.log", "w") as output_file:
                # Run Echidna command with --test-mode assertion flag, redirecting output to file
                echidna_process = subprocess.Popen(
                    ["echidna", "--test-mode", "assertion", self.file_path],
                    stdout=output_file,
                    stderr=subprocess.STDOUT,  # Merge stderr into stdout
                )

                # Wait for 10 seconds
                time.sleep(10)

                # Send the ESC character signal to the process
                echidna_process.send_signal(subprocess.signal.SIGINT)
                logger.info("Sent ESC character signal to Echidna process.")

        except subprocess.CalledProcessError as e:
            logger.error(f"Echidna failed with error: {e}")
        except FileNotFoundError:
            logger.error(
                "Echidna executable not found. Please make sure Echidna is installed and added to your PATH."
            )

    def start_echidna_thread(self):
        # Run Echidna in a separate thread
        echidna_thread = threading.Thread(target=self.run_echidna)
        echidna_thread.start()

        # Wait for the thread to finish
        echidna_thread.join()
