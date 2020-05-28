from error_exit import error_exit

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
			error_exit("Bad Syntax, missing =>")
		if rule.count('=') != 1 or rule.count('>') != 1:
			error_exit("Bad Syntax, two implies in one rule")
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
		for fact in self.facts:
			if initial_fact == fact.symbol:
				fact.initialize_true()
				fact.deduce_true()
				break
		self.initial_facts.append(initial_fact)

	def add_queries(self, query):
		found_fact = False
		if not query.isalpha():
			error_exit("Non-alphabet character in query")
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
