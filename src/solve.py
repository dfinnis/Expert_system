from error import check_error
from error_exit import error_exit
from parenthesis import parse_parenthesis
from print_logic import print_logic
from solve_rule import solve_rule

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
	## Deduce undetermined
	for content in children:
		if "|" in content or "^" in content or undetermined:
			for child in content:
				if child.isalpha():
					for fact in g.facts:
						if child == fact.symbol:
							fact.deduce_undetermined()
							rules = append_rule(child, rules, g)
	
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
