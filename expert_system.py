import argparse

def parse_args():
    my_parser = argparse.ArgumentParser(description="Expert system solves propositional calculus.")
    my_parser.add_argument('Filepath',
                       metavar='filepath',
                       type=str,
                       help='provide a valid input file. Rules, facts and queries')
    args = my_parser.parse_args()
    filepath = args.Filepath
    return filepath

class fact:

    def __init__(self, symbol):
        print("I, {}, am initialized".format(symbol))############
        self.symbol = symbol
        self.rules = []

    def add_rule(self, rule):
        print("I am adding rule {}".format(rule))##############
        self.rules.append(rule)

def main():
    try:
        filepath = parse_args()
        print(filepath)

        f = fact('A')
        f.add_rule('=> B')
        f.add_rule('=> C')
        print(f.rules)

        print("Oh hi!")######!!!!!
    except:
        print("Error")

if __name__ == '__main__':
    main()