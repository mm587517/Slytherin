import re


class LogAnalyzer:

    @staticmethod
    def check_failure():
        with open("echidna_output.log", "r") as file:
            for line in file:
                if "failed!💥" in line:
                    return True
        return False

    @staticmethod
    def analyze_log():
        print("Analyzing log...")
        # Define a regex pattern for matching timestamps
        date_pattern = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{2}\]"

        with open("echidna_output.log", "r") as file:
            block_info = ""
            capturing_block = False
            for line in file:

                if re.search(date_pattern, line):
                    if capturing_block:

                        print("=" * 50)
                        print(block_info)
                        print("=" * 50)
                        return
                    block_info = ""
                if "failed!💥" in line:
                    capturing_block = True
                if capturing_block:

                    block_info += line

        if capturing_block:

            print("=" * 50)
            print(block_info)
            print("=" * 50)
