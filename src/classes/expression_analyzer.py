from slither.core.expressions.binary_operation import (
    BinaryOperation,
    BinaryOperationType,
)
from slither.core.expressions.tuple_expression import TupleExpression
from slither.core.expressions.literal import Literal
from slither.core.expressions.identifier import Identifier
from slither.core.expressions.expression import Expression
from slither.core.expressions.type_conversion import TypeConversion
from slither.core.expressions.assignment_operation import AssignmentOperation
from slither.core.expressions.call_expression import CallExpression


from slither.core.solidity_types.type import Type
from slither.core.variables.variable import Variable


from slither.core.expressions import *


from IPython import embed

from loguru import logger

from test_file_generator import TestFileGenerator


logger.add("loguru.log")


class ExpressionAnalyzer:
    @staticmethod
    def type_battle(left: Type, right: Type) -> Type:
        if left.storage_size[0] > right.storage_size[0]:
            return left
        else:
            return right

    @staticmethod
    def get_inverse_operation(operation_type: BinaryOperation) -> BinaryOperationType:
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
        cls, expression: Expression, test_file_generator: TestFileGenerator
    ) -> Type:

        # logger.debug(f"{expression} -- {type(expression)}")

        if isinstance(expression, BinaryOperation):
            left_expresssion = expression.expression_left
            right_expression = expression.expression_right

            left_type = cls.find_expression_elementary_type(
                expression=left_expresssion, test_file_generator=test_file_generator
            )
            right_type = cls.find_expression_elementary_type(
                expression=right_expression, test_file_generator=test_file_generator
            )

            winner = cls.type_battle(left=left_type, right=right_type)

            inverse_operation = cls.get_inverse_operation(
                expression.type,
            )

            assert_string = f"assert ({left_expresssion} <= type({winner}).max {inverse_operation} {right_expression}); //slytherin"
            test_file_generator.write_line(
                target=str(expression), line_to_insert=assert_string
            )

            return winner

        elif isinstance(expression, TupleExpression):
            types = [
                cls.find_expression_elementary_type(
                    expression=sub_expression, test_file_generator=test_file_generator
                )
                for sub_expression in expression.expressions
            ]

            return max(types, key=lambda t: t.storage_size[0])

        elif isinstance(expression, Identifier):
            value = expression.value
            if isinstance(value, Variable):
                return value.type

        elif isinstance(expression, Literal):
            return expression.type

        return None

    @staticmethod
    def contains_binary_operation(expression: Expression) -> bool:
        if isinstance(expression, BinaryOperation):
            return True
        if isinstance(expression, AssignmentOperation):
            return ExpressionAnalyzer.contains_binary_operation(
                expression=expression.expression_right
            )
        if isinstance(expression, CallExpression):
            for argument in expression.arguments:
                return ExpressionAnalyzer.contains_binary_operation(expression=argument)

        logger.debug(f"{expression} -- {type(expression)}")
        if isinstance(expression, TupleExpression):
            return any(
                ExpressionAnalyzer.contains_binary_operation(expression=exp)
                for exp in expression.expressions
            )

        return False
