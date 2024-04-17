import os
import re


class TestFileGenerator:
    def __init__(self, filename: str) -> None:
        self.filename: str = filename
        file_name, extension = os.path.splitext(os.path.basename(filename))

        self.output_filename: str = os.path.join(
            "output", f"{file_name}.experiment{extension}"
        )

        self.create_output_file()
        self.number = 1

    def create_output_file(self) -> None:
        """Creates output file for the test cases"""
        with open(self.filename, "r") as f_in, open(self.output_filename, "w") as f_out:
            for line in f_in:
                f_out.write(line)

    def whitespace_remover(self, text: str) -> str:
        """Removes white spaces in a string

        Args:
            text (str): text to remove strings

        Returns:
            str: string with removed white spaces
        """
        return "".join(text.split())

    def is_substring(self, source: str, target: str) -> bool:
        """Checks if string is substring of another

        Args:
            source (str): string in question
            target (str): string we wish to find

        Returns:
            bool: _description_
        """
        return self.whitespace_remover(target) in self.whitespace_remover(source)

    def write_line(self, target: str, line_to_insert: str, function_name: str) -> None:
        """Writes a line to a file at certain spot

        Args:
            target (str): line we wish to write above of
            line_to_insert (str): line to be written
            function_name (str): function name to ensure we write in the correct place
        """
        with open(self.output_filename, "r") as f_in, open(
            self.output_filename + ".temp", "w"
        ) as f_out:
            flag = False

            pattern = rf"function {function_name}\s*\("
            for line in f_in:
                if re.search(pattern, line):
                    flag = True
                if self.is_substring(line, target) and flag:
                    # Maintain the same leading whitespaces
                    leading_spaces = len(line) - len(line.lstrip())
                    whitespace = " " * leading_spaces
                    f_out.write(f"{whitespace}{line_to_insert} {self.number}\n")
                    self.number += 1
                    flag = False
                f_out.write(line)
            import os

            os.remove(self.output_filename)
            os.rename(self.output_filename + ".temp", self.output_filename)
