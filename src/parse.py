import argparse
import os
from error_exit import error_exit
from objects import graph

def parse_args():
	my_parser = argparse.ArgumentParser(description="Expert system solves propositional calculus.")
	my_parser.add_argument('Filepath',
					   metavar='filepath',
					   type=str,
					   help='provide a valid input file. Rules, facts and queries')
	my_parser.add_argument('-g',
                        '--graph',
                        action='store_true',
                        help='display graph of facts and rules nodes')
	my_parser.add_argument('-c',
                        '--color',
                        action='store_true',
                        help='display output without color, default colored')
	my_parser.add_argument('-t',
                        '--timer',
                        action='store_true',
                        help='display time taken to solve')
	my_parser.add_argument('-l',
                        '--logic',
                        action='store_true',
                        help='display reasoning, visualize logical steps taken')
	args = my_parser.parse_args()
	filepath = args.Filepath
	graph = args.graph
	color = args.color
	timer = args.timer
	logic = args.logic
	return filepath, graph, color, timer, logic

def parse_initial_facts(line, g):
	if g.initial_facts:
		error_exit("Multiple lines of initial facts")
	initial_facts = line
	i = 0
	for letter in initial_facts:
		fact_found = False
		if i > 0:
			if not letter.isalpha():
				error_exit("Non-alphabet character in initial facts")
			for fact in g.facts:
				if letter == fact.symbol:
					fact_found = True
					break
			if fact_found:
				g.add_initial_fact(letter)
			else:
				g.add_fact(letter)
				g.add_initial_fact(letter)
		i += 1
		if i > 26:
			error_exit("Initial facts too long")

def parse_queries(line, g):
	if g.queries:
		error_exit("Multiple lines of queries")
	queries = line
	i = 0
	for letter in queries:
		if i > 0:
			g.add_queries(letter)
		i += 1
		if i > 26:
			error_exit("Queries too long")

def parse_rule(line, g):
	i = 0
	for letter in line:
		i += 1
		if i > 100000:
			error_exit("Rule too long")
		if letter.isalpha() == True:
			found = False
			for fact in g.facts:
				if letter == fact.symbol:
					found = True
			if not found:
				g.add_fact(letter)
	g.add_rule(line)

def parse_file(filepath):
	if not os.path.isfile(filepath):
		error_exit("Invalid filepath")
	allowedSymbols = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '(', ')', '+', '!', '|', '^', '=', '>', '?'}

	g = graph()
	with open(filepath, 'r') as file:
		i = 0
		initial_facts_found = False
		for line in file:
			i += 1
			if i > 10000:
				error_exit("File too long")
			line = line.replace(" ", "").replace("\t", "").replace("\n", "").split("#")[0]
			if line != "":
				if not allowedSymbols.issuperset(line):
					error_exit("Invalid symbol in file")

				if line[0] == '=':
					parse_initial_facts(line, g)
					initial_facts_found = True
				elif line[0] == '?':
					if not initial_facts_found:
						error_exit("Queries given before initial facts")
					parse_queries(line, g)
				else:
					if initial_facts_found:
						error_exit("Rule given after initial facts")
					if g.queries:
						error_exit("Rule given after queries")
					parse_rule(line, g)

		if initial_facts_found == False:
			error_exit("No initial facts")
		if not g.queries:
			error_exit("No queries")

	g.link_facts_rules()
	return g
