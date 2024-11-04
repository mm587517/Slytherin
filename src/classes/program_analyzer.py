from expression_analyzer import ExpressionAnalyzer
from loguru import logger
from slither.slither import Slither
from test_file_generator import TestFileGenerator

logger.add("loguru.log")


class ProgramAnalyzer:
    def __init__(self, filename: str):
        """Initializes the filename

        Args:
            filename (str): solidity file to be analyzed
        """
        self.filename = filename

    def analyze(self):
        """Analyzes all expressions in a file"""
        slither_instance = Slither(self.filename)
        test_file_generator = TestFileGenerator(filename=self.filename)

        for contract in slither_instance.contracts:
            for function in contract.functions:

                for expression in function.expressions:

                    if not ExpressionAnalyzer.contains_binary_operation(
                        expression=expression
                    ):
                        continue

                    ExpressionAnalyzer.expression_dissector(
                        expression=expression,
                        test_file_generator=test_file_generator,
                        function_name=function.name,
                    )
