import re
from echidna_runner import EchidnaRunner


class FileModifier:
    def __init__(self, filename):
        self.filename = filename
        open("echidna_output.log", "w").close()

    def comment_line(self, line):
        return f"// {line.strip()}\n"

    def uncomment_line(self, line):
        return line.lstrip("//").strip() + "\n"

    def find_and_comment(self):
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

            lines_to_uncomment = []

            for i, line in enumerate(lines):
                if "assert" in line and "slytherin" in line:
                    lines[i] = self.comment_line(line)
                    lines_to_uncomment.append(i)

            with open(self.filename, "w") as file:
                file.writelines(lines)

            for index in lines_to_uncomment:
                lines[index] = self.uncomment_line(lines[index])
                with open(self.filename, "w") as file:
                    file.writelines(lines)
                echidna = EchidnaRunner(self.filename)
                echidna.run_echidna()
                lines[index] = self.comment_line(lines[index])
                with open(self.filename, "w") as file:
                    file.writelines(lines)

            # Uncommenting all lines at the end
            for index in lines_to_uncomment:
                lines[index] = self.uncomment_line(lines[index])

            with open(self.filename, "w") as file:
                file.writelines(lines)

        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")


# Example usage:
filename = "output/test.experiment.sol"  # Change this to your file name
modifier = FileModifier(filename)
modifier.find_and_comment()


# Read the log file
with open("echidna_output.log", "r") as file:
    log_data = file.readlines()

# Define regular expression pattern for status line
status_pattern = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] \[status\] tests: \d/\d, fuzzing: \d+/\d+, values: \[\], cov: \d+, corpus: \d+"

# Initialize list to store pairs of consecutive lines
pairs = []

# Iterate through lines to find pairs
for i in range(len(log_data) - 1):
    line1 = log_data[i].strip()
    line2 = log_data[i + 1].strip()
    if re.match(status_pattern, line1) and ("failed" in line2 or "passing" in line2):
        pairs.append((line1, line2))

# Print pairs

print("Failed Test Cases:")
for index, pair in enumerate(pairs):
    if "failed!💥" in pair[1]:
        print(f"\tSlytherin {index+1} failed!💥")
