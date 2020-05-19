import sys

def error_exit(error_msg):###### move somewhere!!!!!!!!!
	print("Error: {}".format(error_msg))
	sys.exit()

def check_syntax(g):
	for rule in g.rules:
		parents = rule.parents.split("+")
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
	check_syntax(g)
	check_loop(g)
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

def solve(g):
	check_error(g)

	for rule in g.rules:#########
		rule.children = rule.children.split("+")#####
		rule.parents = rule.parents.split("+")########
	

	rules = []
	rules_original = []
	for rule in g.rules:
		rules_original.append(rule)
		for parent in rule.parents:
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

	# for rule in rules:#########
		# print("\n\n\x1b[33m#### ---- RULES LIST: {} => {} ----####\x1b[0m".format(rule.parents, rule.children))########
	# for rule in rules_original:#########
	# 	print("\n\n\x1b[34m#### ---- RULES LIST: {} => {} ----####\x1b[0m".format(rule.parents, rule.children))########

	## Apply rules
	while rules:
		for rule in rules:
			# print("\n\n\x1b[35m#### ---- RULE: {} => {} ----####\x1b[0m".format(rule.parents, rule.children))########
			parents = 0
			true = 0
			undetermined = False
			for parent in rule.parents:
				# print("parent = {}".format(parent))##########
				parents += 1

				# print("len(parent) = {}".format(len(parent)))######
				if len(parent) == 1: ## ADD
					# print(parent)####
					for fact in g.facts:
						# print("fact.symbol = {}".format(fact.symbol))#########
						if parent == fact.symbol:
							# print("fact.true = {}".format(fact.deduced_true))#########
							if fact.deduced_true == True:
								# print("fact is true!")#########
								true += 1
							# print(fact.symbol)############
							# print("oh hi")###########
							if fact.undetermined:
								undetermined = True
							break

				elif len(parent) == 2: ## NOT
					# print("\x1b[31mparent = {}\x1b[0m".format(parent))##########
						# if not parent.isalpha():
					
					for fact in g.facts:
						# print("fact.symbol = {}".format(fact.symbol))#########
						if parent[1] == fact.symbol:
							# print("fact.true = {}".format(fact.deduced_true))#########
							if fact.deduced_true == False:
								# print("fact is true!")#########
								true += 1
							if fact.undetermined:
								undetermined = True
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
							for fact in g.facts:
								if parent == fact.symbol:		
									if fact.undetermined:
										undetermined = True
							for fact in g.facts:
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
							# print("\x1b[32mparent = {}\x1b[0m".format(parent))##########
							for fact in g.facts:
								if parent[1] == fact.symbol:
									if fact.undetermined:
										undetermined = True
							for fact in g.facts:
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
									for fact in g.facts:
										if parent == fact.symbol:		
											if fact.undetermined:
												undetermined = True
									for fact in g.facts:
										# print("fact.symbol = {}".format(fact.symbol))#########
										if parent == fact.symbol:
											# print("fact.true = {}".format(fact.deduced_true))#########
											if fact.deduced_true == True:
												# print("xor +1 is true!")#########
												xor_true += 1
												# print("xor_true: {}".format(xor_true))

								elif len(parent) == 2: ## XOR not
									# print("\x1b[32mparent = {}\x1b[0m".format(parent))##########
									for fact in g.facts:
										if parent[1] == fact.symbol:
											if fact.undetermined:
												undetermined = True
									for fact in g.facts:
									# print("fact.symbol = {}".format(fact.symbol))#########
										if parent[1] == fact.symbol:
										# print("fact.true = {}".format(fact.deduced_true))#########
											if fact.deduced_true == False:
											# print("fact is true!")#########
												xor_true += 1
											break

								# else:###########
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
				for child in rule.children:
					# print("child = {}".format(child))
					if len(child) == 1: ## SIMPLE CASE
						# print("child len 1")
						for fact in g.facts:
							if child == fact.symbol:
								# print("child = {}, fact = {}".format(child, fact.symbol))########
								fact.deduce_false()
								### append to rules list??

			## Deduce undetermined
			for child in rule.children:
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
				for child in rule.children:
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