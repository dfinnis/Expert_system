from error_exit import error_exit
from parenthesis import parse_parenthesis

def check_parenthesis(parents):
	if parents.count("(") != parents.count(")"):
		error_exit("Bad Syntax, parenthesis unbalanced")
	_ = parse_parenthesis(parents)

def check_parents(parents):
	parents = parents.replace('(', '').replace(')', '').split("+")
	for parent in parents:
		if not parent:
			error_exit("Bad Syntax, + missing symbol")
		if len(parent) == 1: ## AND
			if not parent.isalpha():
				error_exit("Bad Syntax, non-alphabet symbol")
		elif len(parent) == 2: ## NOT
			if parent[0] != "!" or not parent[1].isalpha():
				error_exit("Bad Syntax, combined conditions")
		else: ## OR / XOR
			parents_or = parent.split("|")
			for parent in parents_or:
				if len(parent) == 1: ## OR
					if not parent.isalpha():
						error_exit("Bad Syntax, non-alphabet symbol with |")
				elif len(parent) == 2: ## OR NOT
					if parent[0] != "!" or not parent[1].isalpha():
						error_exit("Bad Syntax, 2 combined conditions")
				else: ## XOR
					parents_xor = parent.split("^")
					for parent in parents_xor:
						if len(parent) == 1: ## XOR
							if not parent.isalpha():
								error_exit("Bad Syntax, non-alphabet symbol with ^")
						elif len(parent) == 2: ## XOR NOT
							if parent[0] != "!" or not parent[1].isalpha():
								error_exit("Bad Syntax, many combined conditions")
						else:
							for content in parents_xor:
								for letter in content:
									last = letter
									if not (letter == "!" or letter.isalpha()):
										error_exit("Bad Syntax, too many combined conditions")
								if not last.isalpha():
									error_exit("Bad Syntax, too many combined conditions")

def check_children(children):
	if "(" in children or ")" in children:
		error_exit("Bad Syntax, parenthesis in conclusion")
	children = children.split("+")
	for child in children:
		if not child:
			error_exit("Bad Syntax, + missing symbol in conclusion")
		if len(child) == 1: ## AND
			if not child.isalpha():
				error_exit("Bad Syntax, non-alphabet symbol")
		elif len(child) == 2: ## NOT
			if child[0] != "!" or not child[1].isalpha():
				error_exit("Bad Syntax, combined conditions")
		else: ## OR / XOR
			children_or = child.split("|")
			for child_or in children_or:
				if len(child_or) == 1: ## OR
					if not child_or.isalpha():
						error_exit("Bad Syntax, non-alphabet symbol with |")
				elif len(child_or) == 2: ## OR NOT
					if child_or[0] != "!" or not child_or[1].isalpha():
						error_exit("Bad Syntax, 2 combined conditions")
				else: ## XOR
					children_xor = child_or.split("^")
					for child_xor in children_xor:
						if len(child_xor) == 1: ## XOR
							if not child_xor.isalpha():
								error_exit("Bad Syntax, non-alphabet symbol with ^")
						elif len(child_xor) == 2: ## XOR NOT
							if child_xor[0] != "!" or not child_xor[1].isalpha():
								error_exit("Bad Syntax, many combined conditions")
						else:
							error_exit("Bad Syntax, too many combined conditions")

def check_syntax(g):
	for rule in g.rules:
		check_parenthesis(rule.parents)
		check_parents(rule.parents)
		check_children(rule.children)


def check_loop(g):
	for rule in g.rules:
		rules_tree = []
		for child in rule.children:
			for letter in child:
				if letter.isalpha():
					deduced = letter
					for rule_implied in g.rules:
						for parent in rule_implied.parents:
							for letter in parent:
								if letter == deduced:
									rules_tree.append(rule_implied)
					for rule_implied in rules_tree:
						if len(rules_tree) > 420000: ## complexity limit
							error_exit("Bad Logic, infinite loop")
						for child in rule_implied.children:
							for letter in child:
								if letter.isalpha():
									deduced = letter
									for rule_orig in g.rules:
										for parent in rule_orig.parents:
											for letter in parent:
												if letter == deduced:
													if rule_orig.parents == rule.parents and rule_orig.children == rule.children:
														error_exit("circular Logic, infinite loop")
													rules_tree.append(rule_orig)
													break

def check_contradiction(g):
	for fact in g.facts:
		rules_tree = []
		positive = []
		negative = []
		for child_rule in fact.child_rules:
			rules_tree.append(child_rule)
		for child_rule in rules_tree:
			negative_found = False
			for letter in child_rule.children:
				if letter == "!":
					negative_found = True
				if letter.isalpha():
					if negative_found == False:
						positive.append(letter)
					else:
						negative.append(letter)
					negative_found = False		
			for rule_implied in g.rules:
				for parent in rule_implied.parents:
					for letter_implied in parent:
						if letter_implied == letter:
							rules_tree.append(rule_implied)
		for pos in positive:
			for neg in negative:
				if pos == neg:
					error_exit("Bad Logic, contradiction")

def check_error(g):
	check_syntax(g)
	check_loop(g)
	check_contradiction(g)