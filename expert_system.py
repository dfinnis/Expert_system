import argparse
import os

def parse_args():
	my_parser = argparse.ArgumentParser(description="Expert system solves propositional calculus.")
	my_parser.add_argument('Filepath',
					   metavar='filepath',
					   type=str,
					   help='provide a valid input file. Rules, facts and queries')
	args = my_parser.parse_args()
	filepath = args.Filepath
	return filepath

class graph:
	def __init__(self):
		self.facts = []
		self.initial_facts = []
		self.queries = []

class fact:

	def __init__(self, symbol):
		print("I, {}, am initialized".format(symbol))############
		self.symbol = symbol
		self.true = False
		self.rules = []

	def add_rule(self, rule):
		print("I am adding rule {}".format(rule))##############
		self.rules.append(rule)

def main():
	try:
		filepath = parse_args()
		print(filepath)############
		if not os.path.isfile(filepath):
			print("Error: filepath invalid")
			return

		# f = fact('A')
		# f.add_rule('=> B')
		# f.add_rule('=> C')
		# print(f.rules)

		allowedSymbols = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '(', ')', '+', '!', '|', '^', '=', '>', '?'}
		
		with open(filepath, 'r') as file:
			for line in file:
				str = line.replace(" ", "").replace("\t", "").replace("\n", "").split("#")[0]
				if str != "":
					if not allowedSymbols.issuperset(str):
						print("Error: invalid symbol in file")
						return

					print(str)
				# print("oh yeh!")#####

		print("Oh hi!")######!!!!!
	except:
		print("Error")

if __name__ == '__main__':
	main()
		