import re
from echidna_runner import EchidnaRunner
from log_analyzer import LogAnalyzer
from loguru import logger


class FileModifier:
    def __init__(self, filename):
        self.filename = filename
        # Clears file before every run
        with open("echidna_output.log", "w") as log_file:
            log_file.close()

    def comment_line(self, line):
        """Comment a given line of code."""
        return f"// {line.strip()}\n"

    def uncomment_line(self, line):
        """Uncomment a given line of code."""
        return line.lstrip("//").strip() + "\n"

    def get_comment(self, string):
        """Retrieve comment from a string."""
        comment_index = string.find("//")
        if comment_index != -1:
            return string[comment_index + 2 :].strip()
        return "No comment found in the string."

    def find_and_comment(self):
        """Find specific lines, comment them, run tests, and uncomment based on the result."""
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

            lines_to_uncomment = []

            # Comment out specific lines containing 'assert' and 'slytherin'
            for i, line in enumerate(lines):
                if "assert" in line and "slytherin" in line:
                    lines[i] = self.comment_line(line)
                    lines_to_uncomment.append(i)

            # Write the changes back to the file
            with open(self.filename, "w") as file:
                file.writelines(lines)

            # Process each line to uncomment, analyze and revert the comment if necessary
            for index in lines_to_uncomment:
                original_line = self.uncomment_line(lines[index])
                lines[index] = original_line
                with open(self.filename, "w") as file:
                    file.writelines(lines)

                echidna = EchidnaRunner(self.filename)
                echidna.run_echidna()

                if LogAnalyzer.check_failure():
                    test_case_number = self.get_comment(original_line)
                    logger.info(test_case_number)
                    LogAnalyzer.analyze_log()
                else:
                    # Re-comment the line if the test passes
                    lines[index] = self.comment_line(original_line)

                # Restore the commented line regardless of the test result
                with open(self.filename, "w") as file:
                    file.writelines(lines)

            # Ensure all lines are uncommented at the end
            for index in lines_to_uncomment:
                lines[index] = self.uncomment_line(lines[index])

            with open(self.filename, "w") as file:
                file.writelines(lines)

        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")


# Example usage:
