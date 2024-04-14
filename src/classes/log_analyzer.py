import re


class LogAnalyzer:
    @staticmethod
    def analyze_log():
        # Define a regex pattern for matching dates
        date_pattern = (
            r"\[\d{4}-\d{2}-\d{2}"  # Matches dates in the format [YYYY-MM-DD]
        )

        # Open the log file
        with open("echidna_output.log", "r") as file:
            block_info = ""
            call_sequence = ""
            capturing_call_sequence = (
                False  # Flag to indicate if we're capturing the call sequence
            )
            for line in file:
                # Use regex to check if the line contains a date
                if re.search(date_pattern, line):
                    # If block info exists, print it with formatting
                    if block_info:
                        print("=" * 50)  # Separator
                        print("Block Information:")
                        print("-" * 50)  # Separator
                        # Add proper spacing and dashes between different pieces of information
                        formatted_block_info = re.sub(
                            r"([a-zA-Z])(\d)", r"\1 \2", block_info
                        )
                        formatted_block_info = re.sub(
                            r"(?<=[^\d])(?=\d)", " ", formatted_block_info
                        )
                        formatted_block_info = re.sub(
                            r"(?<=\d)([a-zA-Z])", r" -- \1", formatted_block_info
                        )
                        print(formatted_block_info)
                        if call_sequence:
                            print("Call Sequence:")
                            # Indent each call in the sequence
                            print("\t" + call_sequence.strip())
                        break  # Exit loop after printing the first failed block
                    block_info = ""  # Reset block info for new block
                    call_sequence = ""  # Reset call sequence for new block
                    capturing_call_sequence = False  # Reset flag for new block
                elif "failed!💥" in line:
                    # If block failed, add its information to be printed
                    block_info += line
                elif (
                    "Seed" in line
                    or "Corpus size" in line
                    or "Unique instructions" in line
                ):
                    # Add relevant information to block info
                    block_info += line.strip()
                elif "Call sequence:" in line:
                    # Start capturing the call sequence
                    call_sequence += line
                    capturing_call_sequence = True
                elif capturing_call_sequence:
                    # Continue capturing the call sequence until it ends
                    call_sequence += line
                    if line.strip() == "":
                        capturing_call_sequence = False  # End of call sequence
