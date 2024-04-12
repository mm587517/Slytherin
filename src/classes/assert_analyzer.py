import re

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
for index, pair in enumerate(pairs):
    if "failed!💥" in pair[1]:
        print(index)
