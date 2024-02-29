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
