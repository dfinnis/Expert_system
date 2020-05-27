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
	## XOR loop
	parents_xor = parents.split("^")
	# print(parents_xor)#######
	xor_true = 0
	for parent_xor in parents_xor:
		if len(parent_xor) == 1: ## XOR
			# print("\x1b[31mparent 1 = {}\x1b[0m".format(parent))#######
			if parent_xor.isdigit():
				# print("parent digit: {}".format(parent_and))#########
				if parent_xor == "1":
					xor_true += 1
				elif parent_xor == "2":
					undetermined = True
			else:
				for fact in g.facts:
					# print("fact.symbol = {}".format(fact.symbol))#########
					if parent_xor == fact.symbol:
						if fact.undetermined:
							undetermined = True
						# print("fact.true = {}".format(fact.deduced_true))#########
						if fact.deduced_true == True:
							# print("xor +1 is true!")#########
							xor_true += 1
							# print("xor_true: {}".format(xor_true))
						break

		elif len(parent_xor) == 2: ## XOR not
			# print("\x1b[32mparent = {}\x1b[0m".format(parent))##########
			if parent_xor[1].isdigit():
				# print("parent digit: {}".format(parent_and))#########
				if parent_xor[1] == "0":
					xor_true += 1
				elif parent_xor[1] == "2":
					undetermined = True
			else:
				for fact in g.facts:
				# print("fact.symbol = {}".format(fact.symbol))#########
					if parent_xor[1] == fact.symbol:
					# print("fact.true = {}".format(fact.deduced_true))#########
						if fact.undetermined:
							undetermined = True
						if fact.deduced_true == False:
						# print("fact is true!")#########
							xor_true += 1
						break

		else:	## OR loop
			# print("\x1b[31mparent_xor = {}\x1b[0m".format(parent_xor))##########
			parents_or = parent_xor.split("|")
			# print("\x1b[32mparents_or = {}\x1b[0m".format(parents_or))##########
			or_true = False
			for parent_or in parents_or:
				# print("\x1b[32mlen(parent) = {}\x1b[0m".format(len(parent)))##########
				if len(parent_or) == 1: ## OR
					if parent_or.isdigit():
						# print("parent digit: {}".format(parent_and))#########
						if parent_or == "1":
							or_true = True
						elif parent_or == "2":
							undetermined = True
					else:
						for fact in g.facts:
							# print("fact.symbol = {}".format(fact.symbol))#########
							if parent_or == fact.symbol:
								# print("fact.true = {}".format(fact.deduced_true))#########
								if fact.undetermined:
									undetermined = True
								if fact.deduced_true == True:
									or_true = True
								break

				elif len(parent_or) == 2: ## OR NOT
					# print("\x1b[32mparent = {}\x1b[0m".format(parent))##########
					if parent_or[1].isdigit():
						# print("parent digit: {}".format(parent_and))#########
						if parent_or[1] == "0":
							or_true = True
						elif parent_or[1] == "2":
							undetermined = True
					else:
						for fact in g.facts:
						# print("fact.symbol = {}".format(fact.symbol))#########
							if parent_or[1] == fact.symbol:
							# print("fact.true = {}".format(fact.deduced_true))#########
								if fact.undetermined:
									undetermined = True
								if fact.deduced_true == False:
								# print("fact is true!")#########
									# true += 1######
									or_true = True
								break
	
				else:	## AND loop
					parents_and = parent_or.split("+")
					and_count = 0
					and_true = 0
					for parent_and in parents_and:
						and_count += 1
						if len(parent_and) == 1: ## ADD
							# print(parent_and)####
							if parent_and.isdigit():
								# print("parent digit: {}".format(parent_and))#########
								if parent_and == "1":
									and_true += 1
								elif parent_and == "2":
									undetermined = True
							else:
								for fact in g.facts:
									# print("fact.symbol = {}".format(fact.symbol))#########
									if parent_and == fact.symbol:
										# print("fact.true = {}".format(fact.deduced_true))#########
										if fact.undetermined:
											undetermined = True
										if fact.deduced_true == True:
											# print("fact is true!")#########
											and_true += 1
										break

						elif len(parent_and) == 2: ## NOT
							# print("\x1b[31mparent_and = {}\x1b[0m".format(parent_and))##########
								# if not parent_and.isalpha():
							if parent_and[1].isdigit():
								# print("parent digit: {}".format(parent_and))#########
								if parent_and == "0":
									and_true += 1
								elif parent_and == "2":
									undetermined = True
							else:
								for fact in g.facts:
									# print("fact.symbol = {}".format(fact.symbol))#########
									if parent_and[1] == fact.symbol:
										# print("fact.true = {}".format(fact.deduced_true))#########
										if fact.undetermined:
											undetermined = True
										if fact.deduced_true == False:
											# print("fact is true!")#########
											and_true += 1
										break

						else:
							error_exit("Bad Syntax, 2 many combined condtions") ### catch all other errors??!!!!!
					
					if and_true == and_count:
						or_true = True
						# print("or true = {}".format(or_true))########

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

def solve(g, logic):
	check_error(g)
	if logic:
		print("\n\x1b[1m#### ---- VISUALIZE REASONING ---- ####\x1b[0m\n")

	rules = init_rules_list(g)
	while rules:
		for rule in rules:
			parents = parse_parenthesis(rule.parents)
			# print("parents: {}".format(parents))##########
			if isinstance(parents, list):
				# print("\nParents NOW: {}".format(parents))#######
				parents = solve_parenthesis(parents, g)
				# print("\nParents after: {}".format(parents))#######

			xor_true, undetermined = solve_rule(parents, g)

			if "|" in rule.children or "^" in rule.children:
				undetermined = True

			print_logic(logic, rule, xor_true, undetermined, g)

			## Deduce True
			children = rule.children.split("+")
			if xor_true == 1:
				for child in children:
					# print("child = {}".format(child))
					if len(child) == 1: ## SIMPLE CASE
						# print("child len 1")
						for fact in g.facts:
							if child == fact.symbol:
								# print("child = {}, fact = {}".format(child, fact.symbol))								
								# print("deduce true!")
								fact.deduce_true()
								## add rule to list of rules
								for rule_orig in g.rules:
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
													if not rule_in_list(rule_orig, rules):
														rules.append(rule_orig)
					if len(child) == 2: ## NOT!
						for fact in g.facts:
							if child[1] == fact.symbol:
								if fact.initially_true:
									error_exit("Bad Logic, contradiction")

			## Deduce False
			else:
				# print("Make children false")##########
				for child in children:
					# print("child = {}".format(child))
					if len(child) == 1: ## SIMPLE CASE
						# print("child len 1")
						for fact in g.facts:
							if child == fact.symbol:
								# print("child = {}, fact = {}".format(child, fact.symbol))########
								fact.deduce_false()
								### append to rules list?? no

			## Deduce undetermined
			for child in children:
				# print("child = {}".format(child))##########
				if len(child) > 2: #### + len 2 (not)???????????########
					children_or = child.split("|")
					for child in children_or:
						if len(child) == 1:
							for fact in g.facts:
								if child == fact.symbol:
									fact.deduce_undetermined()
									### append to rules list?#########
									for rule_orig in g.rules:
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
														if not rule_in_list(rule_orig, rules):
															rules.append(rule_orig)
						children_xor = child.split("^")
						for child in children_xor:
							if len(child) == 1:
								for fact in g.facts:
									if child == fact.symbol:
										fact.deduce_undetermined()
										### append to rules list?#######
										for rule_orig in g.rules:
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
															if not rule_in_list(rule_orig, rules):
																rules.append(rule_orig)
					
			if undetermined:
				for child in children:
					# print("child = {}".format(child))
					if len(child) == 1: ## SIMPLE CASE
						# print("child len 1")
						for fact in g.facts:
							if child == fact.symbol:
								# print("child = {}, fact = {}".format(child, fact.symbol))########
								fact.deduce_undetermined()
								for rule_orig in g.rules:
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
													if not rule_in_list(rule_orig, rules):
														rules.append(rule_orig)

			rules.remove(rule)

	if logic:
		print