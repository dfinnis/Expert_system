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
		self.symbol = symbol
		self.child_rules = []
		self.parent_rules = []
		self.initially_true = False
		self.deduced_true = False
		self.undetermined = False

	def add_child_rule(self, rule):
		self.child_rules.append(rule)

	def add_parent_rule(self, rule):
		self.parent_rules.append(rule)

	def initialize_true(self):
		self.initially_true = True
	
	def deduce_true(self):
		self.deduced_true = True
	
	def deduce_false(self):
		self.deduced_true = False
	
	def deduce_undetermined(self):
		self.undetermined = True

class rule:
	def __init__(self):
		self.parents = []
		self.children = []

	def parse_rule(self, rule):
		left = rule.split("=>")[0]
		self.parents = left.split("+")
		right = rule.split("=>")[1]
		self.children = right.split("+")

class graph:
	def __init__(self):
		self.facts = [] 
		self.rules = []
		self.initial_facts = []
		self.queries = []

	def add_fact(self, symbol):
		f = fact(symbol)
		self.facts.append(f)

	def add_rule(self, line):
		r = rule()
		r.parse_rule(line)
		self.rules.append(r)

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
		self.initial_facts.append(initial_fact)

	def add_queries(self, query):
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

		rules = []
		rules_original = []
		for rule in self.rules:
			rules_original.append(rule)
			for parent in rule.parents:
				# print("\n\n\x1b[33m#### ---- parent: {} ----####\x1b[0m".format(parent))########
				negative = False
				for letter in parent:
					# print("\n\n\x1b[33m#### ---- letter: {} ----####\x1b[0m".format(letter))########
					if letter.isalpha():
						# print("\n\n\x1b[33m#### ---- letter is alpha ----####\x1b[0m")########
						for fact in self.facts:
							# print("\n\n\x1b[33m#### ---- fact: {} ----####\x1b[0m".format(fact.symbol))########
							if letter == fact.symbol: ############## add not ????!!!!!!!!!!!!
								# print("\n\n\x1b[33m#### ---- letter = fact ----####\x1b[0m")########		
								# print("\n\n\x1b[33m#### ---- fact is {} ----####\x1b[0m".format(fact.initially_true))########
								if negative == False:
									if fact.initially_true == True:
										# print("\n\n\x1b[33m#### ---- fact is true!!!! ----####\x1b[0m")########	
										rules.append(rule)
								else:
									if fact.initially_true == False:
										# print("\n\n\x1b[33m#### ---- fact is true!!!! ----####\x1b[0m")########	
										rules.append(rule)
								break
						negative = False						
					elif letter == "!":
						negative = True

		## Infinite loop check
		for rule in rules_original:
			# print("\n\n\x1b[36m#### ---- RULES LIST: {} => {} ----####\x1b[0m".format(rule.parents, rule.children))########
			rules_tree = []
			for letter in rule.children:
				if letter.isalpha():
					deduced = letter
					for rule_implied in rules_original:
						for letter in rule_implied.parents:
							if letter == deduced:
								rules_tree.append(rule_implied)
					# while rules_tree:
					for rule_implied in rules_tree:
						# print("\n\n\x1b[32m#### ---- RULE IMPLIED: {} => {} ----####\x1b[0m".format(rule_implied.parents, rule_implied.children))########
						for letter in rule_implied.children:
							if letter.isalpha():
								for rule_orig in rules_original:
									# print("\n\n\x1b[34m#### ---- RULE ORIGINAL: {} => {} ----####\x1b[0m".format(rule_orig.parents, rule_orig.children))########
									for parent in rule_orig.parents:
										# print("\x1b[33mparent: {}\x1b[0m".format(parent))##########
										if parent == letter:
											if rule_orig.parents == rule.parents and rule_orig.children == rule.children:
												error_exit("circular Logic, infinite loop")
											rules_tree.append(rule_orig)
											break


		# for rule in rules:#########
			# print("\n\n\x1b[33m#### ---- RULES LIST: {} => {} ----####\x1b[0m".format(rule.parents, rule.children))########
		# for rule in rules_original:#########
		# 	print("\n\n\x1b[34m#### ---- RULES LIST: {} => {} ----####\x1b[0m".format(rule.parents, rule.children))########

		while rules:
			for rule in rules:
				# print("\n\n\x1b[35m#### ---- RULE: {} => {} ----####\x1b[0m".format(rule.parents, rule.children))########
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

								xor_true = 0
								for parent in parents_xor:
									# print("\x1b[32mparent = {}\x1b[0m".format(parent))##########
									if len(parent) == 1: ## XOR
										# print("\x1b[31mparent 1 = {}\x1b[0m".format(parent))##########!!!!!!
										if not parent.isalpha():
											error_exit("Bad Syntax, non-alphabet symbol with ^")## can we get here?!!!!
										for fact in self.facts:
											# print("fact.symbol = {}".format(fact.symbol))#########
											if parent == fact.symbol:
												# print("fact.true = {}".format(fact.deduced_true))#########
												if fact.deduced_true == True:
													# print("xor +1 is true!")#########
													xor_true += 1
													# print("xor_true: {}".format(xor_true))

									elif len(parent) == 2: ## XOR not

										if parent[0] != "!" or not parent[1].isalpha():
											# print("\x1b[32mparent = {}\x1b[0m".format(parent))##########
											error_exit("Bad Syntax, many combined conditions")######## test how can we get here??!!!!!!
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
										# error_exit("Bad Syntax, 2 many combined condtions") ### catch all other errors??!!!!!
									
								if xor_true == 1:
									# print("Here I am!!")
									true += 1
								
				# print("# parents = {}".format(parents))#######
				# print("# true = {}".format(true))########

				## Deduce True
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
											# print(parent_orig)#############
											for letter in parent_orig:
												if letter.isalpha():
													# print(letter)#############
													if child == letter:
														# print("\n\x1b[35m#### ---- APPENDING RULE: {} => {} ----####\x1b[0m".format(rule_orig.parents, rule_orig.children))########
														# print("\n\x1b[35m#### ---- APPENDING RULE: CHILD: {} ----####\x1b[0m".format(child))########
														# print("\n\x1b[35m#### ---- APPENDING RULE: PARENT: {} ----####\x1b[0m".format(parent_orig))########
														rules.append(rule_orig)
						else:
							children_or = child.split("|")
							for child in children_or:
								if len(child) == 1: ## SIMPLE CASE ########
									for fact in self.facts:
										if child == fact.symbol:
											fact.deduce_undetermined()

								children_xor = child.split("^")
								for child in children_xor:
									if len(child) == 1: ## SIMPLE CASE ########
										for fact in self.facts:
											if child == fact.symbol:
												fact.deduce_undetermined()

				## Deduce False
				else:
					# print("Make children false")##########
					for child in rule.children:
						# print("child = {}".format(child))
						if len(child) == 1: ## SIMPLE CASE
							# print("child len 1")
							for fact in self.facts:
								if child == fact.symbol:
									# print("child = {}, fact = {}".format(child, fact.symbol))########
									fact.deduce_false()

				rules.remove(rule)
				# for rule in rules:
				# 	print("\n\n\x1b[1m#### ---- RULES LIST: {} => {} ----####\x1b[0m".format(rule.parents, rule.children))########
				# print ############

	def print_graph(self):

		print("\n\n\x1b[1m#### ---- GRAPH ----####\x1b[0m")
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

	def print_results(self):
		for query in self.queries:
			for fact in self.facts:
				if query == fact.symbol:
					if fact.undetermined == True:
						print("{} is Undetermined".format(query)) ## No color ######### Yellow!!!!!!	
					else:
						print("{} is {}".format(query, fact.deduced_true)) ## No color
						# if fact.true == True:
						# 	print("\x1b[32m{} is True\x1b[0m".format(query))
						# else:
						# 	print("\x1b[31m{} is False\x1b[0m".format(query))		

def error_exit(error_msg):
	print("Error: {}".format(error_msg))
	sys.exit()

def parse(filepath):
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

	g.link_facts_rules()
	return g			

def main():
	try:
		filepath, graph = parse_args()
		g = parse(filepath)
		g.solve()
		if graph:
			g.print_graph()
		g.print_results()
	except:
		pass

if __name__ == '__main__':
	main()

### if all parents true, all children made true
### parenthesis: cut out new rule, put between parent and current rule (append list to list)
### make list of parents/children to process, add add new symbols(facts) to list as children are deduced
### protect against circular logic
### contradiction in the facts, or a syntax error