from slither.slither import Slither
from slither.core.expressions.binary_operation import BinaryOperation
from slither.core.expressions.assignment_operation import AssignmentOperation
from slither.core.expressions.literal import Literal
from slither.core.expressions.identifier import Identifier
from slither.core.expressions.tuple_expression import TupleExpression
from print_helpers import PrintMsg
from print_helpers import PrintContract
from print_helpers import PrintWarning

def Largest(input_1, input_2):
	input_1_str = str(input_1)
	input_2_str = str(input_2)
	index_1 = -1
	index_2 = -1
	for i in range(len(input_1_str)):
		if input_1_str[i:].isdigit():
			input_1_str = input_1_str[i:]
			break
	for i in range(len(input_2_str)):
		if input_2_str[i:].isdigit():
			input_2_str = input_2_str[i:]
			break
	int_1 = int(input_1_str)
	int_2 = int(input_2_str)
	if int_1 > int_2:
		return input_1
	return input_2

def HandleTupleExpression(tuple):
	print('\t\tTupleExpression: ' + str(tuple))
	tuple_list = tuple.expressions
	for tuple in tuple_list:
		if isinstance(tuple, BinaryOperation):
			return HandleBinaryOperation(tuple)
		elif isinstance(tuple, TupleExpression):
			return HandleTupleExpression(tuple)
		elif isinstance(tuple, Identifier):
			return tuple.value.type
		elif isinstacne(tuple, Literal):
			return tuple.type

def HandleBinaryOperation(binary_operation):
	print('\t\tBinaryOperation: ' + str(binary_operation))
	
	right = binary_operation.expression_right
	right_type = ''
	left = binary_operation.expression_left
	left_type = ''	

	if isinstance(right, BinaryOperation):
		HandleBinaryOperation(right)
	elif isinstance(right, TupleExpression):
		HandleTupleExpression(right)
	elif isinstance(right, Identifier):
		right_type = right.value.type
	elif isinstacne(right, Literal):
		right_type = right.type
 
	if isinstance(left, BinaryOperation):
		HandleBinaryOperation(left)
	elif isinstance(left, TupleExpression):
		HandleTupleExpression(left)
	elif isinstance(left, Identifier):
		left_type = left.value.type
	elif isinstance(left, Literal):
		left_type = left.type

	if left_type != right_type:
		PrintWarning('\t\t\tWarning casting between ' + str(right_type) + ' and ' + str(left_type))
		return Largest(left_type, right_type)
	else:
		return left_type

def HandleAssignment(assignment):
	left_type = assignment.expression_return_type
	right = assignment.expression_right
	right_type = ''

	if isinstance(right, BinaryOperation):
		right_type = HandleBinaryOperation(right)
	elif isinstance(right, Identifier):
		right_type = right.value.type
	elif isinstance(right, TupleExpression):
		right_type = HandleTupleExpression(right)
	elif isinstance(right, Literal):
		right_type = right.type

	if left_type != right_type:
		PrintWarning('\t\tWarning casting between ' + str(right_type) + ' to ' + str(left_type))

def IterateContract(slither_instance):
	for contract in slither_instance.contracts:
		PrintContract('Contract: ' + contract.name)
		
		for function in contract.functions:
		
			for expression in function.expressions:
				print('\tExpression: ' + str(expression))
				if isinstance(expression, AssignmentOperation):
					HandleAssignment(expression)
