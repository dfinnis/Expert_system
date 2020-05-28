# import argparse
import time
import sys
sys.path.extend(["./src/"])
from solve import solve
from error_exit import error_exit
from objects import graph
from parse import parse_args
from parse import parse_file

def main():
	try:
		filepath, graph, color, timer, logic = parse_args()
		if timer:
			start = time.time()
		g = parse_file(filepath)
		solve(g, logic)
		if graph:
			g.print_graph()
		g.print_results(color)
		if timer:
			end = time.time()
			time_taken = '%s' % float('%.3g' % (end - start))
			print("time taken: {} seconds".format(time_taken))
	except:
		pass

if __name__ == '__main__':
	main()
