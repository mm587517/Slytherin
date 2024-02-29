from slither.slither import Slither
from slither.core.expressions.binary_operation import BinaryOperation
from slither.core.expressions.assignment_operation import AssignmentOperation
from slither.core.expressions.literal import Literal
from slither.core.expressions.identifier import Identifier
from slither.core.expressions.tuple_expression import TupleExpression
from print_helpers import PrintMsg
from print_helpers import PrintContract
from print_helpers import PrintWarning
from IPython import embed


def FindLargest(x1, x2):
	working_x1 = str(x1)
	working_x2 = str(x2)
	if 'uint' in working_x1:
		x1_size = int(working_x1[4:])
		x2_size = int(working_x2[4:])
		if x1_size > x2_size:
			return x1
		return x2
	elif 'int' in working_x1:
		x1_size = int(working_x1[3:])
		x2_size = int(working_x2[3:])
		if x1_size > x2_size:
			return x1
		return x2

def FindBinaryOperations(expression):
	print('\tExpression: ' + str(expression))
	if isinstance(expression, BinaryOperation):
		print('\t\tBinary Operation Type: ' + str(expression.type))
		print('\t\tLeft Operand: ' + str(expression.expression_left))
		print('\t\tRight Operang: ' + str(expression.expression_right))
		
		if isinstance(expression.expression_right, BinaryOperation):
			FindBinaryOperations(expression.expression_left)
		if isinstance(expression.expression_left, BinaryOperation):
			FindBinaryOperations(expression.expression_right)

def BinaryOperations(expression):
	left_final = expression.expression_return_type
	right = expression.expression_right
	print('\t\tLeft Final: ' + str(left_final))
	if isinstance(right, Literal):
		print('\t\tright type: ' + str(right.type))
	if isinstance(right, BinaryOperation):
		BinaryOperations(right)

def HandleBinaryOperation(expression, variables):
	print('\t\tHandleBinaryOperation: ' + str(expression))
	right = expression.expression_right
	left = expression.expression_left
	right_type = ''
	left_type = ''

	if isinstance(right, BinaryOperation):
		right_type = HandleBinaryOperation(right)
	elif isinstance(right, Identifier):
		right_type = variables[str(right)]
	
	if isinstance(left, BinaryOperation):
		left_type = HandleBinaryOperation(left)
	elif isinstance(left, Identifier):
		left_type = variables[str(left)]
	if  left_type != right_type:
		PrintWarning('\t\t\tWARNING: casting between ' + str(left_type) + ' and ' + str(right_type))
		return FindLargest(left_type, right_type)
	return left_type

def HandleTupleExpression(tuple, variables):
	tuple_list = tuple.expressions
	for tuple in tuple_list:
		if isinstance(tuple, BinaryOperation):
			return HandleBinaryOperation(tuple, variables)
		elif isinstance(tuple, Literal):
			return tuple.type
		elif isinstance(tuple, Identifier):
			return tuple.value.type
		elif isinstance(tuple, TupleExpression):
			return HandleTupleExpression(tuple, variables)
	return None

def HandleAssignmentRight(right, variables):
	if isinstance(right, Literal):
		print('\t\tAssignment Operation -> No Warnings')
		return None
	elif isinstance(right, BinaryOperation):
		return HandleBinaryOperation(right, variables)
	elif isinstance(right, Identifier):
		return right.value.type
	elif isinstance(right, TupleExpression):
		return HandleTupleExpression(right, variables)

def IterateContract(slither_instance):
	for contract in slither_instance.contracts:
		PrintContract('Contract: ' + contract.name)
		
		for function in contract.functions:
			variables = {}
			for expression in function.expressions:
				print('\tExpression: ' + str(expression))
				if isinstance(expression, AssignmentOperation):
					left_type = expression.expression_return_type
					left_name = expression.expression_left
					variables[str(left_name)] = left_type
					print('\t\tleft_name: ' + str(left_name))
					right_type = HandleAssignmentRight(expression.expression_right, variables)
					if left_type != right_type and right_type != None:
						PrintWarning('\t\tWarning casting between ' + str(left_type) + ' and ' + str(right_type))
