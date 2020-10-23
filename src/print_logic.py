def print_logic(logic, rule, xor_true, undetermined, g):
	if logic:
		if undetermined:
			print("\x1b[33m#### ---- Apply rule: {} => {} ---- ####\x1b[0m".format(rule.parents, rule.children))
		elif xor_true == 1:
			print("\x1b[32m#### ---- Apply rule: {} => {} ---- ####\x1b[0m".format(rule.parents, rule.children))
		else:
			print("\x1b[31m#### ---- Apply rule: {} => {} ---- ####\x1b[0m".format(rule.parents, rule.children))
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
				if child.isalpha():
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
