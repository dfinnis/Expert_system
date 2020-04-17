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

def main():
    try:
        filepath = parse_args()
        print(filepath)
        print("Oh hi!")######!!!!!
    except:
        print("Error")

if __name__ == '__main__':
    main()