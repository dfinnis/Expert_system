import argparse
import os
import sys

def parse_args():
	my_parser = argparse.ArgumentParser(description="Expert system solves propositional calculus.")
	my_parser.add_argument('Filepath',
					   metavar='filepath',
					   type=str,
					   help='provide a valid input file. Rules, facts and queries')
	my_parser.add_argument('-g',
                        '--graph',
                        action='store_true',
                        help='Display graph of facts and rules nodes')
	args = my_parser.parse_args()
	filepath = args.Filepath
	graph = args.graph
	return filepath, graph

class fact:

	def __init__(self, symbol):
		# print("I, {}, am initialized".format(symbol))############
		self.symbol = symbol
		self.true = False
		self.child_rules = []
		self.parent_rules = []

	def assign_true(self):
		self.true = True

	def add_child_rule(self, rule):
		# print("I am adding rule {}".format(rule))##############
		self.child_rules.append(rule)

	def add_parent_rule(self, rule):
		# print("I am adding rule {}".format(rule))##############
		self.parent_rules.append(rule)

class rule:

	def __init__(self):
		# pass
		# # self.rule = line
		# # self.rule = 
		self.parents = []
		self.children = []

	def parse_rule(self, rule):
		left = rule.split("=>")[0]
		self.parents = left.split("+")
		right = rule.split("=>")[1]
		self.children = right.split("+")		
		# self.parent = rule.split("=>")[0]
		# self.child = rule.split("=>")[1]

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

	def add_rule(self, line):
		# print(line)######
		r = rule()
		r.parse_rule(line)
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

	def link_facts_rules(self):
		for rule in self.rules:
			# print(rule.parents)#####	
			for parent in rule.parents:
				# print(parent)#
				for letter in parent:
					if letter.isalpha():
						for fact in self.facts:
							if letter == fact.symbol:
								fact.add_child_rule(rule)
			for child in rule.children:
				for letter in child:
					if letter.isalpha():
						for fact in self.facts:
							if letter == fact.symbol:
								fact.add_parent_rule(rule)



			# for letter in rule.parent:
			# 	if letter.isalpha():
			# 		for fact in self.facts:
			# 			if letter == fact.symbol:
			# 				fact.add_child_rule(rule)
			# for letter in rule.child:
			# 	if letter.isalpha():
			# 		for fact in self.facts:
			# 			if letter == fact.symbol:
			# 				fact.add_parent_rule(rule)

	def print_graph(self):

		print("\n\x1b[1mFacts:\x1b[0m")
		for fact in self.facts:
			print(fact.symbol)
			print(fact.true)
			print("Child rules:")
			for rule in fact.child_rules:
				print("rule.parent: {}".format(rule.parents))
				print("rule.child: {}".format(rule.children))
			print("Parent rules:")
			for rule in fact.parent_rules:
				print("rule.parent: {}".format(rule.parents))
				print("rule.child: {}".format(rule.children))
			print

		print("\n\x1b[1mAll Rules:\x1b[0m")
		for rule in self.rules:
			print("rule.parents: {}".format(rule.parents))
			print("rule.children: {}".format(rule.children))

		print("\n\x1b[1mInitial facts:\x1b[0m {}\n".format(self.initial_facts))
		print("\x1b[1mQueries:\x1b[0m {}\n".format(self.queries))

def error_exit(error_msg):
	print("Error: {}".format(error_msg))
	sys.exit()

def parse(filepath):

	# filepath, graph = parse_args()
	if not os.path.isfile(filepath):
		error_exit("Invalid filepath")

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
					for letter in line:
						if letter.isalpha() == True:
							found = False
							for fact in g.facts:
								if letter == fact.symbol:
									found = True
							if not found:
								g.add_fact(letter)
					g.add_rule(line)
					# g.rules.append(line)
					# print(line)

	g.link_facts_rules()
	return g

def print_results(g):
	for query in g.queries:
		for fact in g.facts:
			if query == fact.symbol:
				if fact.true == True:
					print("\x1b[32m{} is True\x1b[0m".format(query))
				else:
					print("\x1b[31m{} is False\x1b[0m".format(query))					

def main():
	try:
		filepath, graph = parse_args()
		g = parse(filepath)
		if graph:
			g.print_graph()
		print_results(g)
		# print("Oh hi!")######!!!!!
	except:
		# print("Error")
		pass

if __name__ == '__main__':
	main()

### if all parents true, all children made true
### parenthesis: cut out new rule, put between parent and current rule