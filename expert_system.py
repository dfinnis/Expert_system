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
		self.child_rules = []
		self.parent_rules = []
		self.initially_true = False
		self.deduced_true = False

	def add_child_rule(self, rule):
		# print("I am adding rule {}".format(rule))##############
		self.child_rules.append(rule)

	def add_parent_rule(self, rule):
		# print("I am adding rule {}".format(rule))##############
		self.parent_rules.append(rule)

	def initialize_true(self):
		self.initially_true = True
	
	def deduce_true(self):
		self.deduced_true = True

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
				fact.initialize_true()
				fact.deduce_true()
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
			for parent in rule.parents:
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

	def solve(self):
		# print("\n\n\x1b[1m#### ----solvingtime! ----####\x1b[0m")##########
		rules = []
		rules_original = []
		# print("\n\n\x1b[33m#### ---- RULES LIST: {} ----####\x1b[0m".format(rules))########
		for rule in self.rules:
			rules.append(rule)
			rules_original.append(rule)
		# for rule in rules:
		# 	print("\n\n\x1b[33m#### ---- RULES LIST: {} => {} ----####\x1b[0m".format(rule.parents, rule.children))########
		# for rule in rules_original:
		# 	print("\n\n\x1b[34m#### ---- RULES LIST: {} => {} ----####\x1b[0m".format(rule.parents, rule.children))########

		while rules:
			for rule in rules:
				# print("rule = {} => {}".format(rule.parents, rule.children))##########
				parents = 0
				true = 0
				for parent in rule.parents:
					# print("parent = {}".format(parent))##########
					parents += 1
					if not parent:
						error_exit("Bad Syntax, + missing symbol")

					# print("len(parent) = {}".format(len(parent)))######
					if len(parent) == 1: ## ADD
						if not parent.isalpha():
							# print("parent = {}".format(parent))##########
							error_exit("Bad Syntax, non-alphabet symbol")
						# print(parent)####
						for fact in self.facts:
							# print("fact.symbol = {}".format(fact.symbol))#########
							if parent == fact.symbol:
								# print("fact.true = {}".format(fact.deduced_true))#########
								if fact.deduced_true == True:
									# print("fact is true!")#########
									true += 1
								break

					elif len(parent) == 2: ## NOT
						# print("\x1b[31mparent = {}\x1b[0m".format(parent))##########
						if parent[0] != "!" or not parent[1].isalpha():
							error_exit("Bad Syntax, combined conditions")
							# if not parent.isalpha():
						
						for fact in self.facts:
							# print("fact.symbol = {}".format(fact.symbol))#########
							if parent[1] == fact.symbol:
								# print("fact.true = {}".format(fact.deduced_true))#########
								if fact.deduced_true == False:
									# print("fact is true!")#########
									true += 1
								break
					
					else: ## OR / XOR / (parenthesis for now)
						# print("\x1b[31mparent = {}\x1b[0m".format(parent))##########
						parents_or = parent.split("|")
						# print("\x1b[32mparent = {}\x1b[0m".format(parent))##########
						found_true = False
						for parent in parents_or:
							# print("\x1b[32mlen(parent) = {}\x1b[0m".format(len(parent)))##########
							if len(parent) == 1: ## OR
								# print("\x1b[31mparent 1 = {}\x1b[0m".format(parent))##########
								if not parent.isalpha():
									error_exit("Bad Syntax, non-alphabet symbol with |")
								for fact in self.facts:
									# print("fact.symbol = {}".format(fact.symbol))#########
									if parent == fact.symbol:
										# print("fact.true = {}".format(fact.deduced_true))#########
										if fact.deduced_true == True:
											# print("fact is true!")#########
											true += 1
											found_true = True
										break
								if found_true == True:
									break

							elif len(parent) == 2: ## OR NOT
								if parent[0] != "!" or not parent[1].isalpha():
									# print("\x1b[32mparent = {}\x1b[0m".format(parent))##########
									error_exit("Bad Syntax, 2 combined conditions")
								# print("\x1b[32mparent = {}\x1b[0m".format(parent))##########
								for fact in self.facts:
								# print("fact.symbol = {}".format(fact.symbol))#########
									if parent[1] == fact.symbol:
									# print("fact.true = {}".format(fact.deduced_true))#########
										if fact.deduced_true == False:
										# print("fact is true!")#########
											true += 1
										break

							else: ## XOR
								# print("\x1b[32mparent = {}\x1b[0m".format(parent))##########
								parents_xor = parent.split("^")
								# print("\x1b[32mparent = {}\x1b[0m".format(parent))##########

								# found_true = False
								xor_true = 0
								for parent in parents_xor:
									# print("\x1b[32mparent = {}\x1b[0m".format(parent))##########
									if len(parent) == 1: ## XOR
									# 	# print("\x1b[31mparent 1 = {}\x1b[0m".format(parent))##########
										if not parent.isalpha():
											error_exit("Bad Syntax, non-alphabet symbol with ^")## can we get here?!!!!
										for fact in self.facts:
									# 		# print("fact.symbol = {}".format(fact.symbol))#########
											if parent == fact.symbol:
									# 			# print("fact.true = {}".format(fact.deduced_true))#########
												if fact.deduced_true == True:
													# print("xor +1 is true!")#########
													xor_true += 1

									elif len(parent) == 2: ## XOR not

										if parent[0] != "!" or not parent[1].isalpha():
											# print("\x1b[32mparent = {}\x1b[0m".format(parent))##########
											error_exit("Bad Syntax, many combined conditions")
										# print("\x1b[32mparent = {}\x1b[0m".format(parent))##########
										for fact in self.facts:
										# print("fact.symbol = {}".format(fact.symbol))#########
											if parent[1] == fact.symbol:
											# print("fact.true = {}".format(fact.deduced_true))#########
												if fact.deduced_true == False:
												# print("fact is true!")#########
													xor_true += 1
												break

									# else:
										# error_exit("Bad Syntax, 2 many combined condtions")
									
								if xor_true == 1:
									true += 1
								




				# print("# parents = {}".format(parents))#######
				# print("# true = {}".format(true))########

				if parents == true:
					# print("Make children true")##########
					for child in rule.children:
						# print("child = {}".format(child))
						if len(child) == 1: ## SIMPLE CASE
							# print("child len 1")
							for fact in self.facts:
								if child == fact.symbol:
									# print("child = {}, fact = {}".format(child, fact.symbol))								
									# print("deduce true!")
									fact.deduce_true()
									## add rule to list of rules
									for rule_orig in rules_original:
										# print("\n\x1b[35m#### ---- APPENDING RULE: RULE ORIG = {} => {} ----####\x1b[0m".format(rule_orig.parents, rule_orig.children))########
										for parent_orig in rule_orig.parents:
											if child == parent_orig:
												# print("\n\x1b[35m#### ---- APPENDING RULE: {} => {} ----####\x1b[0m".format(rule_orig.parents, rule_orig.children))########
												# print("\n\x1b[35m#### ---- APPENDING RULE: CHILD: {} ----####\x1b[0m".format(child))########
												# print("\n\x1b[35m#### ---- APPENDING RULE: PARENT: {} ----####\x1b[0m".format(parent_orig))########
												rules.append(rule_orig)
				rules.remove(rule)
				# for rule in rules:
				# 	print("\n\n\x1b[1m#### ---- RULES LIST: {} => {} ----####\x1b[0m".format(rule.parents, rule.children))########
				# print ############

	def print_graph(self):

		print("\n\n\x1b[1m#### ---- GRAPH ----####\x1b[0m")## before/after
		print("\n\x1b[1mRules:\x1b[0m")
		for rule in self.rules:
			print("{} => {}".format(rule.parents, rule.children))

		print("\n\x1b[1mInitial facts:\x1b[0m {}\n".format(self.initial_facts))
		print("\x1b[1mQueries:\x1b[0m {}\n".format(self.queries))

		print("\x1b[1mFacts:\x1b[0m")
		for fact in self.facts:
			print(fact.symbol)
			print("initially true = {}".format(fact.initially_true))
			print("deduced true =   {}".format(fact.deduced_true))
			print("child rules:")
			for rule in fact.child_rules:
				print("{} => {}".format(rule.parents, rule.children))
			print("parent rules:")
			for rule in fact.parent_rules:
				print("{} => {}".format(rule.parents, rule.children))
			print
		print

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
				print("{} is {}".format(query, fact.deduced_true)) ## No color
				# if fact.true == True:
				# 	print("\x1b[32m{} is True\x1b[0m".format(query))
				# else:
				# 	print("\x1b[31m{} is False\x1b[0m".format(query))					

def main():
	try:
		filepath, graph = parse_args()
		g = parse(filepath)
		# if graph:
		# 	g.print_graph()
		g.solve()
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
### parenthesis: cut out new rule, put between parent and current rule (append list to list)
### make list of parents/children to process, add add new symbols(facts) to list as children are deduced
### protect against circular logic