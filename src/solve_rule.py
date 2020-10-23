from error_exit import error_exit

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
			xor_true, undetermined = solve_or(parent_xor, xor_true, undetermined, g)
	return xor_true, undetermined

def solve_or(parent_xor, xor_true, undetermined, g):
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
			or_true, undetermined = solve_and(parent_or, or_true, undetermined, g)

	if or_true:
		xor_true += 1
	return xor_true, undetermined

def solve_and(parent_or, or_true, undetermined, g):
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
	return or_true, undetermined
