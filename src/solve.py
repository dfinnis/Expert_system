from error import check_error
from error_exit import error_exit
from parenthesis import parse_parenthesis

### replace parenthesis with 0 = false, 1 = true, 2 = undetermined
def solve_parenthesis(parents, g):
	solved_str = ""
	contains_list = False
	for parent in parents:
		if isinstance(parent, list):
			contains_list = True
	if contains_list:
		for parent in parents:
			if isinstance(parent, list):
				solved_str += solve_parenthesis(parent, g)
			else:
				solved_str += parent
	else:
		for content in parents:
			xor_true, undetermined = solve_rule(content, g)
			if undetermined:
				solved_str += "2"
			elif xor_true == 1:
				solved_str += "1"
			else:
				solved_str += "0"
	xor_true, undetermined = solve_rule(solved_str, g)
	if undetermined:
		solved_str = "2"
	elif xor_true == 1:
		solved_str = "1"
	else:
		solved_str = "0"
	return solved_str

def solve_rule(parents, g):
	undetermined = False
	parents_xor = parents.split("^")
	xor_true = 0
	## XOR loop
	for parent_xor in parents_xor:
		if len(parent_xor) == 1: ## XOR
			if parent_xor.isdigit():
				if parent_xor == "1":
					xor_true += 1
				elif parent_xor == "2":
					undetermined = True
			else:
				for fact in g.facts:
					if parent_xor == fact.symbol:
						if fact.undetermined:
							undetermined = True
						if fact.deduced_true == True:
							xor_true += 1
						break

		elif len(parent_xor) == 2: ## XOR not
			if parent_xor[1].isdigit():
				if parent_xor[1] == "0":
					xor_true += 1
				elif parent_xor[1] == "2":
					undetermined = True
			else:
				for fact in g.facts:
					if parent_xor[1] == fact.symbol:
						if fact.undetermined:
							undetermined = True
						if fact.deduced_true == False:
							xor_true += 1
						break

		else: ## OR loop
			parents_or = parent_xor.split("|")
			or_true = False
			for parent_or in parents_or:
				if len(parent_or) == 1: ## OR
					if parent_or.isdigit():
						if parent_or == "1":
							or_true = True
						elif parent_or == "2":
							undetermined = True
					else:
						for fact in g.facts:
							if parent_or == fact.symbol:
								if fact.undetermined:
									undetermined = True
								if fact.deduced_true == True:
									or_true = True
								break

				elif len(parent_or) == 2: ## OR NOT
					if parent_or[1].isdigit():
						if parent_or[1] == "0":
							or_true = True
						elif parent_or[1] == "2":
							undetermined = True
					else:
						for fact in g.facts:
							if parent_or[1] == fact.symbol:
								if fact.undetermined:
									undetermined = True
								if fact.deduced_true == False:
									or_true = True
								break
	
				else: ## AND loop
					parents_and = parent_or.split("+")
					and_count = 0
					and_true = 0
					for parent_and in parents_and:
						and_count += 1
						if len(parent_and) == 1: ## ADD
							if parent_and.isdigit():
								if parent_and == "1":
									and_true += 1
								elif parent_and == "2":
									undetermined = True
							else:
								for fact in g.facts:
									if parent_and == fact.symbol:
										if fact.undetermined:
											undetermined = True
										if fact.deduced_true == True:
											and_true += 1
										break

						elif len(parent_and) == 2: ## NOT
							if parent_and[1].isdigit():
								if parent_and == "0":
									and_true += 1
								elif parent_and == "2":
									undetermined = True
							else:
								for fact in g.facts:
									if parent_and[1] == fact.symbol:
										if fact.undetermined:
											undetermined = True
										if fact.deduced_true == False:
											and_true += 1
										break

						else: ## catch all other errors
							error_exit("Bad Syntax, 2 many combined condtions")
					
					if and_true == and_count:
						or_true = True

			if or_true:
				xor_true += 1
	return xor_true, undetermined

def print_logic(logic, rule, xor_true, undetermined, g):
	if logic:
		if undetermined:
			print("\x1b[33m#### ---- Apply rule: {} => {} ----####\x1b[0m".format(rule.parents, rule.children))
		elif xor_true == 1:
			print("\x1b[32m#### ---- Apply rule: {} => {} ----####\x1b[0m".format(rule.parents, rule.children))
		else:
			print("\x1b[31m#### ---- Apply rule: {} => {} ----####\x1b[0m".format(rule.parents, rule.children))
		for parent in rule.parents:
			if parent.isalpha():
				for fact in g.facts:
					if fact.symbol == parent:
						if fact.undetermined:
							print("\x1b[33m{} is Undetermined\x1b[0m".format(parent))
						elif fact.deduced_true:
							print("\x1b[32m{} is True\x1b[0m".format(parent))
						else:
							print("\x1b[31m{} is False\x1b[0m".format(parent))
		if undetermined:
			print("\x1b[33m---- Antecedent Undetermined ----\x1b[0m")
			for child in rule.children:
				print("\x1b[33mConsequent deduced Undetermined: {}\x1b[0m".format(child))
		elif xor_true == 1:
			print("\x1b[32m---- Antecedent determined True ----\x1b[0m")
			children = rule.children.split("+")
			for child in children:
				if len(child) == 1: ## +
					if child.isalpha():
						print("\x1b[32mConsequent deduced True: {}\x1b[0m".format(child))
				elif len(child) == 2: ## !
					if child[1].isalpha():
						print("\x1b[31mConsequent deduced False: {}\x1b[0m".format(child[1]))
				else: ## | ^
					for letter in child:
						if letter.isalpha():
							print("\x1b[33mConsequent deduced Undetermined: {}\x1b[0m".format(letter))
		else:
			print("\x1b[31m---- Antecedent False ----\x1b[0m")
		print

def rule_in_list(rule, rules):
	for rule_already in rules:
		if rule.parents == rule_already.parents and rule.children == rule_already.children:
			return True
	return False

def init_rules_list(g):
	rules = []
	for rule in g.rules:
		parents = rule.parents.split("+")
		for parent in parents:
			negative = False
			for letter in parent:
				if letter.isalpha():
					for fact in g.facts:
						if letter == fact.symbol:
							if negative == False:
								if fact.initially_true == True:
									if not rule_in_list(rule, rules):
										rules.append(rule)
							else:
								if fact.initially_true == False:
									if not rule_in_list(rule, rules):
										rules.append(rule)
							break
					negative = False						
				elif letter == "!":
					negative = True
	return rules

def append_rule(child, rules, g):
	for rule_orig in g.rules:
		for parent_orig in rule_orig.parents:
			for letter in parent_orig:
				if letter.isalpha():
					if child == letter:
						if not rule_in_list(rule_orig, rules):
							rules.append(rule_orig)
	return rules

def deduce(children, rules, g, xor_true, undetermined):
	## Deduce True
	children = children.split("+")
	if xor_true == 1:
		for child in children:
			if len(child) == 1: ## SIMPLE CASE
				for fact in g.facts:
					if child == fact.symbol:
						fact.deduce_true()
						rules = append_rule(child, rules, g)

			if len(child) == 2: ## NOT!
				for fact in g.facts:
					if child[1] == fact.symbol:
						if fact.initially_true:
							error_exit("Bad Logic, contradiction")

	## Deduce False
	else:
		for child in children:
			if len(child) == 1: ## SIMPLE CASE
				for fact in g.facts:
					if child == fact.symbol:
						fact.deduce_false()

	## Deduce undetermined
	for content in children:
		if "|" in content or "^" in content or undetermined:
			for child in content:
				if child.isalpha():
					for fact in g.facts:
						if child == fact.symbol:
							fact.deduce_undetermined()
							rules = append_rule(child, rules, g)
	return rules

def solve(g, logic):
	check_error(g)
	if logic:
		print("\n\x1b[1m#### ---- VISUALIZE REASONING ---- ####\x1b[0m\n")

	rules = init_rules_list(g)
	while rules:
		for rule in rules:
			parents = parse_parenthesis(rule.parents)
			if isinstance(parents, list):
				parents = solve_parenthesis(parents, g)

			xor_true, undetermined = solve_rule(parents, g)

			if "|" in rule.children or "^" in rule.children:
				undetermined = True

			print_logic(logic, rule, xor_true, undetermined, g)

			deduce(rule.children, rules, g, xor_true, undetermined)

			rules.remove(rule)

	if logic:
		print