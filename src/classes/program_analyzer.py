from slither.slither import Slither
from slither.core.expressions.binary_operation import BinaryOperation
from slither.core.expressions.tuple_expression import TupleExpression

from slither.core.expressions.assignment_operation import AssignmentOperation

from test_file_generator import TestFileGenerator
from expression_analyzer import ExpressionAnalyzer

from loguru import logger

logger.add("loguru.log")


class ProgramAnalyzer:
    def __init__(self, filename):
        self.filename = filename

    def analyze(self):
        slither_instance = Slither(self.filename)
        test_file_generator = TestFileGenerator(filename=self.filename)

        flag = False

        for contract in slither_instance.contracts:
            for function in contract.functions:
                for expression in function.expressions:
                    if isinstance(expression, AssignmentOperation):
                        if isinstance(
                            expression.expression_right,
                            (BinaryOperation, TupleExpression),
                        ):

                            flag = True

                            ExpressionAnalyzer.find_expression_elementary_type(
                                expression=expression.expression_right,
                                test_file_generator=test_file_generator,
                            )
        if flag:
            logger.success(f"Created {test_file_generator.output_filename}")
