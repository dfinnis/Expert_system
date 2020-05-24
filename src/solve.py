from error import check_error
from error import error_exit

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

def parenthesis_to_list(contents):
	parenthesis = contents[contents.find("(")+1:]
	# print("parenthesis 1 {}".format(parenthesis))##
	right_i = find_bracket(parenthesis)
	# print("right_i {}".format(right_i))####
	parenthesis = [parenthesis[:right_i]]
	# print("parenthesis 2 {}".format(parenthesis))##
	# # contents_tmp = []
	# # parenthesis_found = False
	# for content in parenthesis:
	# 	print("content before {}".format(content))##
	# 	if "(" in content:
	# 		# parenthesis_found = True
	# 		content = parenthesis_to_list(content)
	# 		print("TRIPLE!!")
	# 		print("content after {}".format(content))##
	# 		print
	# 		# contents_tmp.append(content)
	# 		# parenthesis = content###????
	# 		# parenthesis.append(content)
	# # if contents_tmp:
	# # 	print("PARENTHESIS: {}".format(parenthesis))		
	# # 	print("CONTENT TMP: {}".format(contents_tmp))
	# 	# parenthesis.append(contents_tmp)
	# 	# parenthesis = contents_tmp
		
	if parenthesis == [""]:
		error_exit("Bad syntax, parenthesis empty (())")##### can we get here?!!!!

	contents_parsed = []
	left = contents.split("(")[0]
	if left:
		contents_parsed.append(left)
	
	contents_parsed.append(parenthesis)


	# if isinstance(parenthesis, str):
	# 	contents_parsed.append(parenthesis)
	# else:
	# 	for item in parenthesis:
	# 		contents_parsed.append(item)

	
	right = contents[right_i+2+len(left):]
	if "(" in right:
		right = parenthesis_to_list(right)
	if right:
		if isinstance(right, str):
			contents_parsed.append(right)
		else:
			for item in right:
				contents_parsed.append(item)
	# print("contents_parsed {}".format(contents_parsed))########
	# list_parsed.append(contents_parsed)
	return contents_parsed

def parse_parenthesis(parents):
	# if parents.count("(") != parents.count(")"):
	# 	error_exit("Bad syntax, parenthesis unbalanced")

	if isinstance(parents, str):
		if "(" in parents or ")" in parents:

			parenthesis = parents[parents.find("(")+1:]
			right_i = find_bracket(parenthesis)
			parenthesis = [parenthesis[:right_i]]

			if parenthesis == [""]:
				error_exit("Bad syntax, parenthesis empty ()")##### can we get here?!!!!
			left = parents.split("(")[0]
			right = parents[right_i+2:]
			if "(" in right:
				right = parenthesis_to_list(right)
			parents_parsed = []
			if left:
				parents_parsed.append(left)
			parents_parsed.append(parenthesis)
			if right:
				# parents_parsed.append(right)
				if isinstance(right, str):
					parents_parsed.append(right)
				else:
					for item in right:
						parents_parsed.append(item)
			# print("rule_parsed:	{}".format(parents_parsed))######
			# print("parents:	{}".format(parents))######
			parents = [parents]##########  do this earlier, deal with lists!!!!!!!??
			# print("parents:	{}".format(parents))######
			parents = parents_parsed
			# print("parents string:	{}".format(parents))######
		# if isinstance(parents, list):
			# print("parents list: {}".format(parents))

	if isinstance(parents, list):
		# print("parents again: {}".format(parents))
		# 	for sublist in parents:
		# 		# print(sublist)######
		# 		if isinstance(sublist, list):
		# 			for contents in sublist:
		# 				# print(contents)#####
		# 				if "(" in contents:
		# 					parse_parenthesis(parents)
		# 					print("oh hi!!")

		list_parsed = []
		parenthesis_found = False
		for sublist in parents:
			# print("sublist pre {}".format(sublist))#######

			if isinstance(sublist, list):
				for contents in sublist:
					# print("contents 1 {}".format(contents))##					
					if "(" in contents:
						parenthesis_found = True
						contents_parsed = parenthesis_to_list(contents)
						list_parsed.append(contents_parsed)
					# else:

			else:
				# print("sublist str {}".format(sublist))#######
				list_parsed.append(sublist)
		# print("list_parsed {}".format(list_parsed))	########
		if parenthesis_found:
			# print("oh hi!")#####
			# for sublist in parents:
			# 	if isinstance(sublist, list):
			# 		for contents in sublist:			
			# 			if "(" in contents:
			# 				# print(sublist)######
			# 				parse_parenthesis(parents)
			# 				print("oh hi!!")
			parents = list_parsed
			# else
	# if "(" in parents or ")" in parents:
		### call me again!!

	# print("parents final: {}".format(parents))######
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

	## Create list of rules to evaluate
	rules = []
	rules_original = []
	for rule in g.rules:
		# _ = parse_parenthesis(rule.parents)############ change to just error check, DRY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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
	
			parents = parse_parenthesis(rule.parents)
			# print("parents: {}".format(parents))##########
			if isinstance(parents, list):
				parents = solve_parenthesis(parents, g)

			xor_true, undetermined = solve_rule(parents, g)

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