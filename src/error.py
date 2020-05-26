import sys

def error_exit(error_msg):###### move somewhere!!!!!!!!!
	print("Error: {}".format(error_msg))
	sys.exit()

def check_parenthesis(parents):
	if parents.count("(") != parents.count(")"):
		error_exit("Bad syntax, parenthesis unbalanced")

def check_syntax(g):
	for rule in g.rules:
		check_parenthesis(rule.parents)
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
		# rules_tree_orig = []######
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
									# rules_tree_orig.append(rule_implied)#####
					# while rules_tree:
					# print(len(rules_tree))########
					# for rule_implied in rules_tree_orig:#########
					# 	print("\n\n\x1b[32m#### ---- RULE IMPLIED: {} => {} ----####\x1b[0m".format(rule_implied.parents, rule_implied.children))########
					for rule_implied in rules_tree:
						# print(len(rules_tree))########
						if len(rules_tree) > 420000:######## Lazy hack!!! is this number right?
							error_exit("Bad Logic, infinite loop")
						# print("\n\n\x1b[32m#### ---- RULE IMPLIED: {} => {} ----####\x1b[0m".format(rule_implied.parents, rule_implied.children))########
						for child in rule_implied.children:
							for letter in child:
								if letter.isalpha():
									deduced = letter

									# for rule_tree_orig in rules_tree_orig:
									# 	if rule_tree_orig.parents == rule.parents and rule_tree_orig.children == rule.children:
									# 		error_exit("circular Logic, infinite loop")

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

def check_contradiction(g):
	for fact in g.facts:
		rules_tree = []
		positive = []
		negative = []
		for child_rule in fact.child_rules:
		# 	rules_tree.append(child_rule)
		# for child_rule in rules_tree:
			# print("child_rule.children {}".format(child_rule.children))
			negative_found = False
			for letter in child_rule.children:
				if letter == "!":
					# print("negative!!!!")#######
					negative_found = True
				if letter.isalpha():
					if negative_found == False:
						positive.append(letter)
					else:
						negative.append(letter)
					negative_found = False
				# print("letter {}".format(letter))######
				# print#########
				# for children in child_rule.children:
				# 	print(children)
		for pos in positive:
			# print("positive: {}".format(pos))######
			for neg in negative:
				# print("negative: {}".format(neg))####
				if pos == neg:
					error_exit("Bad Logic, contradiction")


# def check_contradiction(g):
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


def check_error(g):
	check_syntax(g)
	check_loop(g)
	check_contradiction(g)