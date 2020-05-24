import sys

def error_exit(error_msg):###### move somewhere!!!!!!!!!
	print("Error: {}".format(error_msg))
	sys.exit()

def check_syntax(g):
	for rule in g.rules:
		parents = rule.parents.replace('(', '').replace(')', '').split("+")
		for parent in parents:
			if not parent:
				error_exit("Bad Syntax, + missing symbol")
			if len(parent) == 1: ## ADD
				if not parent.isalpha():
					error_exit("Bad Syntax, non-alphabet symbol")
			elif len(parent) == 2: ## NOT
				if parent[0] != "!" or not parent[1].isalpha():
					error_exit("Bad Syntax, combined conditions")
			else: ## OR / XOR / (parenthesis for now)
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
								error_exit("Bad Syntax, too many combined conditions")

def check_loop(g):
	for rule in g.rules:
		# print("\n\n\x1b[36m#### ---- RULES LIST: {} => {} ----####\x1b[0m".format(rule.parents, rule.children))########
		rules_tree = []
		for child in rule.children:
			for letter in child:
				# print(letter)#######
				if letter.isalpha():
					deduced = letter
					# print(deduced)###
					for rule_implied in g.rules:
						for parent in rule_implied.parents:
							for letter in parent:
								if letter == deduced:
									rules_tree.append(rule_implied)
					# while rules_tree:
					for rule_implied in rules_tree:
						# print("\n\n\x1b[32m#### ---- RULE IMPLIED: {} => {} ----####\x1b[0m".format(rule_implied.parents, rule_implied.children))########
						for child in rule_implied.children:
							for letter in child:
								if letter.isalpha():
									deduced = letter
									for rule_orig in g.rules:
										# print("\n\n\x1b[34m#### ---- RULE ORIGINAL: {} => {} ----####\x1b[0m".format(rule_orig.parents, rule_orig.children))########
										for parent in rule_orig.parents:
											# print("\x1b[33mparent: {}\x1b[0m".format(parent))##########
											for letter in parent:
												if letter == deduced:
													if rule_orig.parents == rule.parents and rule_orig.children == rule.children:
														error_exit("circular Logic, infinite loop")
													rules_tree.append(rule_orig)
													break

def check_error(g):
	check_loop(g)
	# for rule in g.rules:
		# parents = rule.parents
		# parents = parents.replace('(', '').replace(')', '')
	check_syntax(g)

	## Contradiction check
	# for rule in rules_original:
	# 	# print("\n\n\x1b[36m#### ---- RULES LIST: {} => {} ----####\x1b[0m".format(rule.parents, rule.children))########
	# 	rules_tree = []
	# 	positive = []
	# 	negative = []
	# 	inverse = False
	# 	for parent in rule.parents:
	# 		for letter in parent:
	# 			if letter == "!":
	# 				inverse = True
	# 			if letter.isalpha():
	# 				if inverse:
	# 					negative.append(parent[1])
	# 					inverse = False
	# 				else:
	# 					positive.append(parent)
	# 	for alpha in positive:##########
	# 		print("+ve: {}".format(alpha))#########
	# 	for alpha in negative:#########
	# 		print("-ve: {}".format(alpha))######

		# for child in rule.children:
		# 	for letter in child:
		# # 		# print(letter)#######
		# 		if letter.isalpha():
		# 			deduced = letter
		# # 			# print(deduced)###
		# 			for rule_implied in rules_original:
		# 				for parent in rule_implied.parents:
		# 					for letter in parent:
		# 						if letter == deduced:
		# 							rules_tree.append(rule_implied)
		# 			# while rules_tree:
		# 			for rule_implied in rules_tree:
		# 				# print("\n\n\x1b[32m#### ---- RULE IMPLIED: {} => {} ----####\x1b[0m".format(rule_implied.parents, rule_implied.children))########
		# 				for child in rule_implied.children:
		# 					for letter in child:
		# 						if letter.isalpha():
		# 							deduced = letter
		# 							for rule_orig in rules_original:
		# 								# print("\n\n\x1b[34m#### ---- RULE ORIGINAL: {} => {} ----####\x1b[0m".format(rule_orig.parents, rule_orig.children))########
		# 								for parent in rule_orig.parents:
		# 									# print("\x1b[33mparent: {}\x1b[0m".format(parent))##########
		# 									for letter in parent:
		# 										if letter == deduced:
		# 											if rule_orig.parents == rule.parents and rule_orig.children == rule.children:
		# 												error_exit("circular Logic, infinite loop")
		# 											rules_tree.append(rule_orig)
		# 											break

def find_bracket(parents):
	i = 0
	pair = 0
	for letter in parents:
		if letter == "(":
			pair += 1
		elif letter == ")":
			if pair == 0:
				return i
			else:
				pair -= 1
		i += 1
	error_exit("Bad syntax, parenthesis")

def parse_parenthesis(parents):
	# for rule in g.rules:
	# while "(" in parents or ")" in parents:### deal with parenthesis inside parenthesis (())
	if "(" in parents or ")" in parents:
		if parents.count("(") != parents.count(")"):
			error_exit("Bad syntax, parenthesis unbalanced")

		# print("parents:	{}".format(parents))######
		# print(parents.find("("))####
		parenthesis = parents[parents.find("(")+1:]		
		# parenthesis = parents.split("(")[1]
		# print(parenthesis.find("("))####
		# parenthesis = parents[parents.find("("):]
		# print("parenthesis:	{}".format(parenthesis))######
		right_i = find_bracket(parenthesis)
		parenthesis = [parenthesis[:right_i]]
		if parenthesis == [""]:
			error_exit("Bad syntax, parenthesis empty ()")##### can we get here?!!!!
		left = parents.split("(")[0]
		right = parents[right_i+2:]####???? +2 ok?!!!

		parents_parsed = []
		if left:
			parents_parsed.append(left)		
		# parents_parsed = left		
		parents_parsed.append(parenthesis)
		if right:
			parents_parsed.append(right)
		# print("rule_parsed:	{}".format(parents_parsed))######
		# print("parents:	{}".format(parents))######
		parents = [parents]##########  do this earlier, deal with lists!!!!!!!??
		# print("parents:	{}".format(parents))######
		parents = parents_parsed
		# print("parents:	{}".format(parents))######
		## if isinstance(parent, list): #### to identify list in list
	return parents

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

def solve_parenthesis(parents, g): ## replace parenthesis with 0 = false, 1 = true, 2 = undetermined
	# print("parents before:	{}".format(parents))
	solved_str = ""
	for parent in parents:
		# print("parent:	{}".format(parent))####
		# print(type(parent))#########
		if isinstance(parent, list):
			# print("list!")######
			for content in parent:
				# print(content)#######
				xor_true, undetermined = solve_rule(content, g)
				# print("xor_true: {}".format(xor_true))#####
				# print("undetermined: {}".format(undetermined))#####
				if undetermined:
					solved_str += "2"
				elif xor_true == 1:
					solved_str += "1"
				else:
					solved_str += "0"			
		else:
			solved_str += parent
	# print("solved_str: {}".format(solved_str))
	return solved_str

def solve(g):
	# parse_parenthesis(g)#####rm!!!!!!
	check_error(g)## PUT ME BACK!!!!!!!!!!!!

	rules = []
	rules_original = []
	for rule in g.rules:
		_ = parse_parenthesis(rule.parents)
		rules_original.append(rule)
		parents = rule.parents.split("+")
		for parent in parents:
			# print("\n\n\x1b[33m#### ---- parent: {} ----####\x1b[0m".format(parent))########
			negative = False
			for letter in parent:
				# print("\n\n\x1b[33m#### ---- letter: {} ----####\x1b[0m".format(letter))########
				if letter.isalpha():
					# print("\n\n\x1b[33m#### ---- letter is alpha ----####\x1b[0m")########
					for fact in g.facts:
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

	## Apply rules
	while rules:
		for rule in rules:
			# print("\n\n\x1b[35m#### ---- RULE: {} => {} ----####\x1b[0m".format(rule.parents, rule.children))########
			rule.parents = parse_parenthesis(rule.parents)##### rm rule. ??
			if isinstance(rule.parents, list):
				rule.parents = solve_parenthesis(rule.parents, g)##### rm rule. ??

			xor_true, undetermined = solve_rule(rule.parents, g)##### rm rule. ??
			
			# parents = parse_parenthesis(parents)##### rm rule. ??
			# if isinstance(parents, list):
			# 	parents = solve_parenthesis(parents, g)##### rm rule. ??

			# xor_true, undetermined = solve_rule(parents, g)##### rm rule. ??

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
								### append to rules list??

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
						children_xor = child.split("^")
						for child in children_xor:
							if len(child) == 1:
								for fact in g.facts:
									if child == fact.symbol:
										fact.deduce_undetermined()
										### append to rules list?#######
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
					
			if undetermined:
				for child in children:
					# print("child = {}".format(child))
					if len(child) == 1: ## SIMPLE CASE
						# print("child len 1")
						for fact in g.facts:
							if child == fact.symbol:
								# print("child = {}, fact = {}".format(child, fact.symbol))########
								fact.deduce_undetermined()
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

			rules.remove(rule)
			# for rule in rules:
			# 	print("\n\n\x1b[1m#### ---- RULES LIST: {} => {} ----####\x1b[0m".format(rule.parents, rule.children))########
			# print ############