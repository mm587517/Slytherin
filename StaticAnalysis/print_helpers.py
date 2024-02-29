from colorama import Fore, Back, Style

def PrintMsg(msg):
	print(Fore.GREEN + msg, end='')
	print(Style.RESET_ALL)

def PrintContract(msg):
	print(Fore.BLUE + msg, end='')
	print(Style.RESET_ALL)

def PrintWarning(msg):
	print(Fore.MAGENTA + msg, end='')
	print(Style.RESET_ALL)
