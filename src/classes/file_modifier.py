from echidna_runner import EchidnaRunner
from log_analyzer import LogAnalyzer
from loguru import logger


class FileModifier:
    def __init__(self, filename):
        """Determines the file to be used for experiments

        Args:
            filename (_type_): experiment run
        """
        self.filename = filename
        # Clears file before every run
        with open("echidna_output.log", "w") as log_file:
            log_file.close()

    def comment_line(self, line: str) -> str:
        """Comments out line in experiment file

        Args:
            line (str): line to be commented out
        Returns:
            str: new line with comment
        """
        return f"// {line.strip()}\n"

    def uncomment_line(self, line: str) -> str:
        """Uncomments out line in experiment file

        Args:
            line (str): line to uncomment

        Returns:
            str: new uncommented line
        """
        return line.lstrip("//").strip() + "\n"

    def get_comment(self, line: str) -> str:
        """Retrieves the comment of a line -- used to determine test case number

        Args:
            line (str): line to be analyzed

        Returns:
            str: actual comment
        """

        comment_index = line.find("//")
        if comment_index != -1:
            return line[comment_index + 2 :].strip()
        return "No comment found in the line."

    def find_and_comment(self):
        """Finds and comments/uncomments all test cases to run one at a time to determine results"""
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
                    print(f"================== {test_case_number} ==================")
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
