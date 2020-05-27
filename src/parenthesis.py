from error_exit import error_exit

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
	if isinstance(parents, str):
		if "(" in parents or ")" in parents:
			parents = [parents]
	if isinstance(parents, list):
		list_parsed = []
		parenthesis_found = False
		for part in parents:
			if "(" in part:
				parenthesis_found = True

				left = part.split("(")[0]
				if left:
					list_parsed.append(left)
			
				parenthesis = part[part.find("(")+1:]
				right_i = find_bracket(parenthesis)
				parenthesis = parenthesis[:right_i]
				parenthesis = [parenthesis]
				if parenthesis == [""]:
					error_exit("Bad syntax, parenthesis empty ()")
				for content in parenthesis:
					if "(" in content:
						parenthesis = parse_parenthesis(parenthesis) ## recursive parse [inside]()
				list_parsed.append(parenthesis)

				right = part[right_i+2+len(left):]
				if "(" in right:
					right = parse_parenthesis(right) ## recursive parse [](right)
					for part in right:
						list_parsed.append(part)				
				elif right:
					list_parsed.append(right)
		if parenthesis_found:
			parents = list_parsed
	return parents

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
