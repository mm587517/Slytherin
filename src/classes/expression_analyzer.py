from loguru import logger
from slither.core.expressions import *
from slither.core.expressions.assignment_operation import AssignmentOperation
from slither.core.expressions.binary_operation import (
    BinaryOperation,
    BinaryOperationType,
)
from slither.core.expressions.call_expression import CallExpression
from slither.core.expressions.expression import Expression
from slither.core.expressions.identifier import Identifier
from slither.core.expressions.literal import Literal
from slither.core.expressions.tuple_expression import TupleExpression
from slither.core.expressions.type_conversion import TypeConversion
from slither.core.solidity_types.type import Type
from slither.core.variables.variable import Variable
from test_file_generator import TestFileGenerator

logger.add("loguru.log")


class ExpressionAnalyzer:

    @staticmethod
    def get_storage_size(type_str: str) -> int:
        """Function to get the storage size of a type when in string format.
        (Arguments to functions are like this... it was annoying)

        Args:
            type_str (str): _description_

        Raises:
            ValueError: _description_

        Returns:
            int: _description_
        """
        # Assuming type_str is in the format 'int8', 'uint256', etc.
        if type_str.startswith("uint"):
            return int(type_str[4:]) // 8  # Divide by 8 to get the size in bytes
        elif type_str.startswith("int"):
            return int(type_str[3:]) // 8  # Divide by 8 to get the size in bytes
        else:
            raise ValueError("Invalid type string")

    @staticmethod
    def type_battle(left, right):
        """Given two types in a binary expression, determine the overall type of the cast if any.

        Args:
            left (_type_): type of left expression
            right (_type_): type of right expression

        Returns:
            _type_: the type of the overall expression
        """
        left_size = right_size = (
            0  # Default size for cases where left or right is a string.
        )

        if isinstance(left, str):
            left_size = ExpressionAnalyzer.get_storage_size(left)
        elif isinstance(left, Type):
            left_size = left.storage_size[0]

        if isinstance(right, str):
            right_size = ExpressionAnalyzer.get_storage_size(right)
        elif isinstance(right, Type):
            right_size = right.storage_size[0]

        if left_size > right_size:
            return left
        else:
            return right

    @staticmethod
    def get_inverse_operation(operation_type: BinaryOperation) -> BinaryOperationType:
        """Function determines the inverse of a binary operation. Used to create automatic test cases

        Args:
            operation_type (BinaryOperation): mathematical operator used

        Returns:
            BinaryOperationType: _description_
        """
        if operation_type == BinaryOperationType.ADDITION:
            return BinaryOperationType.SUBTRACTION
        elif operation_type == BinaryOperationType.SUBTRACTION:
            return BinaryOperationType.ADDITION
        elif operation_type == BinaryOperationType.MULTIPLICATION:
            return BinaryOperationType.DIVISION
        elif operation_type == BinaryOperationType.DIVISION:
            return BinaryOperationType.MULTIPLICATION
        else:
            return None

    @classmethod
    def find_expression_elementary_type(
        cls,
        expression: Expression,
        test_file_generator: TestFileGenerator,
        function_name: str,
    ) -> Type:
        """Function breaks down expressions into different cases to be analyzed and test cases written

        Args:
            expression (Expression): expression that needs type finding
            test_file_generator (TestFileGenerator): file to write to

        Returns:
            Type: type of overall expression
        """

        if isinstance(expression, BinaryOperation):
            left_expresssion = expression.expression_left
            right_expression = expression.expression_right

            left_type = cls.find_expression_elementary_type(
                expression=left_expresssion,
                test_file_generator=test_file_generator,
                function_name=function_name,
            )
            right_type = cls.find_expression_elementary_type(
                expression=right_expression,
                test_file_generator=test_file_generator,
                function_name=function_name,
            )

            winner = cls.type_battle(left=left_type, right=right_type)

            inverse_operation = cls.get_inverse_operation(
                expression.type,
            )

            if not inverse_operation:
                return winner

            assert_string = f"assert ({left_expresssion} <= type({winner}).max {inverse_operation} {right_expression}); //slytherin"
            test_file_generator.write_line(
                target=str(expression),
                line_to_insert=assert_string,
                function_name=function_name,
            )

            return winner

        elif isinstance(expression, TupleExpression):
            types = [
                cls.find_expression_elementary_type(
                    expression=sub_expression,
                    test_file_generator=test_file_generator,
                    function_name=function_name,
                )
                for sub_expression in expression.expressions
            ]

            return max(types, key=lambda t: t.storage_size[0])

        elif isinstance(expression, CallExpression):
            for argument in expression.arguments:

                ExpressionAnalyzer.find_expression_elementary_type(
                    expression=argument,
                    test_file_generator=test_file_generator,
                    function_name=function_name,
                )

            return expression.type_call

        elif isinstance(expression, Identifier):
            value = expression.value
            if isinstance(value, Variable):
                return value.type

        elif isinstance(expression, Literal):
            return expression.type

        return None

    @staticmethod
    def contains_binary_operation(expression: Expression) -> bool:
        """Determines if an expression contains a binary expression

        Args:
            expression (Expression): expression to be analyzed

        Returns:
            bool: result if it contains binary expression
        """
        if isinstance(expression, BinaryOperation):
            return True
        if isinstance(expression, AssignmentOperation):
            return ExpressionAnalyzer.contains_binary_operation(
                expression=expression.expression_right
            )
        if isinstance(expression, CallExpression):
            return any(
                ExpressionAnalyzer.contains_binary_operation(expression=exp)
                for exp in expression.arguments
            )

        if isinstance(expression, TupleExpression):
            return any(
                ExpressionAnalyzer.contains_binary_operation(expression=exp)
                for exp in expression.expressions
            )

        if isinstance(expression, TypeConversion):
            return ExpressionAnalyzer.contains_binary_operation(
                expression=expression.expression
            )

        return False

    @staticmethod
    def expression_dissector(
        expression: Expression,
        test_file_generator: TestFileGenerator,
        function_name: str,
    ):
        """Determines how to proceed with certain expression

        Args:
            expression (Expression): expression in question
            test_file_generator (TestFileGenerator): output file
        """
        if isinstance(expression, AssignmentOperation):
            ExpressionAnalyzer.find_expression_elementary_type(
                expression=expression.expression_right,
                test_file_generator=test_file_generator,
                function_name=function_name,
            )

        elif isinstance(expression, BinaryOperation):
            ExpressionAnalyzer.find_expression_elementary_type(
                expression=expression,
                test_file_generator=test_file_generator,
                function_name=function_name,
            )

        elif isinstance(expression, CallExpression):
            for argument in expression.arguments:
                ExpressionAnalyzer.find_expression_elementary_type(
                    expression=argument,
                    test_file_generator=test_file_generator,
                    function_name=function_name,
                )

        elif isinstance(expression, TypeConversion):
            ExpressionAnalyzer.find_expression_elementary_type(
                expression=expression.expression,
                test_file_generator=test_file_generator,
                function_name=function_name,
            )
