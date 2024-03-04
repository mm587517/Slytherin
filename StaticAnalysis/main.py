import sys
from slither.slither import Slither
from slither.core.expressions.binary_operation import BinaryOperation
from slither.core.expressions.assignment_operation import AssignmentOperation
from helper_functions_2 import IterateContract
from print_helpers import PrintMsg

def main():
	PrintMsg('STARTING')
	print()
	sol_file = sys.argv[1]
	txt_file = sys.argv[2]
	if sol_file != 'none':
		PrintMsg('SINGLE FILE: ' + sol_file)
		print()
		IterateContract(Slither(sol_file))
	elif txt_file != 'none':
		PrintMsg('BATCH FILE: ' + txt_file)
		print()
		file = open(txt_file)
		file_names = file.readLines()
		for file_name in file_names:
			if file_name != '':
				IteraterContract(file_name)
	else:
		PrintMsg('A solution file or txt file is required.')
main()
