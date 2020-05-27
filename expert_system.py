import argparse
import time
import os
import sys
sys.path.extend(["./src/"])
from solve import solve
from error_exit import error_exit

def parse_args():
	my_parser = argparse.ArgumentParser(description="Expert system solves propositional calculus.")
	my_parser.add_argument('Filepath',
					   metavar='filepath',
					   type=str,
					   help='provide a valid input file. Rules, facts and queries')
	my_parser.add_argument('-g',
                        '--graph',
                        action='store_true',
                        help='display graph of facts and rules nodes')
	my_parser.add_argument('-c',
                        '--color',
                        action='store_true',
                        help='display output without color, default colored')
	my_parser.add_argument('-t',
                        '--timer',
                        action='store_true',
                        help='display time taken to solve')
	my_parser.add_argument('-l',
                        '--logic',
                        action='store_true',
                        help='display reasoning, visualize logical steps taken')
	args = my_parser.parse_args()
	filepath = args.Filepath
	graph = args.graph
	color = args.color
	timer = args.timer
	logic = args.logic
	return filepath, graph, color, timer, logic

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
		if not "=>" in rule:
			error_exit("Bad syntax, missing =>")
		if rule.count('=') != 1 or rule.count('>') != 1:
			error_exit("Bad Syntax, two implies in one rule")
		# left = rule.split("=>")[0]######
		# # self.parents = left.split("+")########
		# right = rule.split("=>")[1]#######
		# # self.children = right.split("+")#######
		self.parents = rule.split("=>")[0]
		self.children = rule.split("=>")[1]

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

	def print_graph(self):
		print("\n\x1b[1m#### ---- GRAPH ---- ####\x1b[0m")
		print("\n\x1b[1mRules:\x1b[0m")
		for rule in self.rules:
			print("{} => {}".format(rule.parents, rule.children))

		print("\n\x1b[1mInitial facts:\x1b[32m {}\x1b[0m\n".format(self.initial_facts))
		print("\x1b[1mQueries:\x1b[0m {}\n\n".format(self.queries))

		print("\x1b[1mFacts:\x1b[0m")
		for fact in self.facts:
			if fact.deduced_true:
				print("\x1b[32m{}\x1b[0m".format(fact.symbol))
			else:
				print("\x1b[31m{}\x1b[0m".format(fact.symbol))
			if fact.initially_true:
				print("\x1b[32minitially true = True\x1b[0m")
			else:
				print("\x1b[31minitially true = False\x1b[0m")
			if fact.deduced_true:
				print("\x1b[32mdeduced true = True\x1b[0m")
			else:
				print("\x1b[31mdeduced true = False\x1b[0m")
			if fact.undetermined:
				print("\x1b[33mundetermined = True\x1b[0m")
			else:
				print("undetermined = False")
			print("child rules:")
			for rule in fact.child_rules:
				print("{} => {}".format(rule.parents, rule.children))
			print("parent rules:")
			for rule in fact.parent_rules:
				print("{} => {}".format(rule.parents, rule.children))
			print
		print

	def print_results(self, color):
		for query in self.queries:
			for fact in self.facts:
				if query == fact.symbol:
					if color:
						if fact.undetermined:
							print("{} is Undetermined".format(query))
						else:
							print("{} is {}".format(query, fact.deduced_true))
					else:
						if fact.undetermined:
							print("\x1b[33m{} is Undetermined\x1b[0m".format(query))
						else:
							if fact.deduced_true == True:
								print("\x1b[32m{} is True\x1b[0m".format(query))
							else:
								print("\x1b[31m{} is False\x1b[0m".format(query))

def parse(filepath):
	if not os.path.isfile(filepath):
		error_exit("Invalid filepath")

	allowedSymbols = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '(', ')', '+', '!', '|', '^', '=', '>', '?'}
		
	g = graph()

	with open(filepath, 'r') as file:
		i = 0
		initial_facts_found = False
		for line in file:
			i += 1
			if i > 10000:
				error_exit("File too long")
			line = line.replace(" ", "").replace("\t", "").replace("\n", "").split("#")[0]
			if line != "":
				if not allowedSymbols.issuperset(line):
					error_exit("Invalid symbol in file")

				if line[0] == '=':
					initial_facts_found = True
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

		if initial_facts_found == False:
			error_exit("No initial facts")
		if not g.queries:
			error_exit("No queries")

	g.link_facts_rules()
	return g

def main():
	try:
		filepath, graph, color, timer, logic = parse_args()
		if timer:
			start = time.time()
		g = parse(filepath)
		# g.solve()#######
		solve(g, logic)
		if graph:
			g.print_graph()
		g.print_results(color)
		if timer:
			end = time.time()
			time_taken = '%s' % float('%.3g' % (end - start))
			print("time taken: {} seconds".format(time_taken))
	except:
		pass

if __name__ == '__main__':
	main()

### if all parents true, all children made true
### parenthesis: cut out new rule, put between parent and current rule (append list to list)
### make list of parents/children to process, add add new symbols(facts) to list as children are deduced
### contradiction in the facts, or a syntax error