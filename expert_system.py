import argparse
import os
import sys

def parse_args():
	my_parser = argparse.ArgumentParser(description="Expert system solves propositional calculus.")
	my_parser.add_argument('Filepath',
					   metavar='filepath',
					   type=str,
					   help='provide a valid input file. Rules, facts and queries')
	args = my_parser.parse_args()
	filepath = args.Filepath
	return filepath

class fact:

	def __init__(self, symbol):
		# print("I, {}, am initialized".format(symbol))############
		self.symbol = symbol
		self.true = False
		self.rules = []

	def assign_true(self):
		self.true = True

	# def add_rule(self, rule):
	# 	print("I am adding rule {}".format(rule))##############
	# 	self.rules.append(rule)

class rule:

	def __init__(self):
		self.rule = rule
		self.left = []
		self.right = []

	def parse_rule(self, rule):
		for letter in rule:
			print(letter)

class graph:
	def __init__(self):
		self.facts = [] # pointers to all facts
		self.rules = [] # pointers to all rules
		self.initial_facts = [] #
		self.queries = []

	def add_fact(self, symbol):
		# print("I am adding inital fact {}".format(initial_fact))##############
		f = fact(symbol)
		self.facts.append(f)

	def add_rule(self, rule):
		r = rule()
		r.parse_rule(rule)
		self.rules.append(r)
		## link facts to rule

	def add_initial_fact(self, initial_fact):
		assigned_true = False
		for fact in self.facts:
			if initial_fact == fact.symbol:
				fact.assign_true()
				assigned_true = True
				break
		if not assigned_true:
			error_exit("Inital fact not in rules")
		self.initial_facts.append(initial_fact)#######??????

	def add_queries(self, query):
		# print("I am adding queries {}".format(queries))##############
		found_fact = False
		for fact in self.facts:
			if query == fact.symbol:
				found_fact = True
				break
		if not found_fact:
			error_exit("Query not in rules")
		self.queries.append(query)

	def print_graph(self):

		print("Facts:")
		for fact in self.facts:
			print(fact.symbol)
			print(fact.true)

		print("\nRules: {}\n".format(self.rules))
		print("Initial facts: {}\n".format(self.initial_facts))
		print("Queries: {}\n".format(self.queries))

def error_exit(error_msg):
	print("Error: {}".format(error_msg))
	sys.exit()

def parse():

	filepath = parse_args()
	if not os.path.isfile(filepath):
		error_exit("Invalid filepath")

	# f = fact('A')
	# f.add_rule('=> B')
	# f.add_rule('=> C')
	# print(f.rules)

	allowedSymbols = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '(', ')', '+', '!', '|', '^', '=', '>', '?'}
		
	g = graph()

	with open(filepath, 'r') as file:
		for line in file:
			line = line.replace(" ", "").replace("\t", "").replace("\n", "").split("#")[0]
			if line != "":
				if not allowedSymbols.issuperset(line):
					error_exit("Invalid symbol in file")

				if line[0] == '=':
					if g.initial_facts:
						error_exit("Multiple lines of initial facts")
					initial_facts = line.split("=")[1]
					for letter in initial_facts:
						g.add_initial_fact(letter)

				elif line[0] == '?':
					if g.queries:
						error_exit("Multiple lines of queries")
					queries = line.split("?")[1]
					for letter in queries:
						g.add_queries(letter)

				else:
					# g.add_rule(line)
					g.rules.append(line)
					for letter in line:
						if letter.isalpha() == True:
							if letter not in g.facts:
								g.add_fact(letter)
					# print(line)
	return g

def main():
	try:
		g = parse()
		g.print_graph()
		print("Oh hi!")######!!!!!
	except:
		# print("Error")
		pass

if __name__ == '__main__':
	main()
		