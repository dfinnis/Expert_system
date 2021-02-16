# Expert System

An expert system for propositional calculus, written in python.

A forward-chaining inference engine.

Accepts a list of rules, facts, and queries. It applies logic, then for each query it prints True/False/Undetermined.

## Getting Started

Simply clone this repo.

### Usage

Run with input filepath as argument

![Usage](https://github.com/dfinnis/expert-system/blob/master/img/usage.png?raw=true)

### input file formatting

Input files contain rules, initial facts and queries in the following format.
```
# this is a comment, spacing is not important

A     => B    # Rule: A implies B
A + B => C    # Rule: A and B implies D

=A            # Initial facts: A is true

?B            # Queries: is B true?
```

All facts not initially true are initially false. i.e. B is initially false, but deduced true.

### Logical operations

The following symbols are defined, in order of decreasing priority:

| Symbol | Meaning     | Example           |
| ------ | ----------- | ----------------- |
| ()     | Parenthesis | A + (B \| C) => D |
| \+     | AND         | A + B             |
| \|     | OR          | A \| B            |
| ˆ      | XOR         | A ˆ B             |
| =>     | implies     | A + B => C        |

### Examples

Let's have a look at an example input file, and run it with expert system.

![Example_and_2](https://github.com/dfinnis/expert-system/blob/master/img/example_and_2.png?raw=true)

#### Undetermined

If the consequent is determined true, but includes or / xor, then the truth of the consequent facts is undetermined.

Let's clarify with an example.

![Undetermined](https://github.com/dfinnis/expert-system/blob/master/img/undetermined.png?raw=true)


### Dependencies

Python

## Tests

Run the test script ```./test.sh```.
The test script runs input files from the ```input``` folder, and ensures the output is correct.

Tests are grouped into and, or, xor, not, same conclusion, parenthesis and error tests.

![Tests](https://github.com/dfinnis/expert-system/blob/master/img/tests.gif)

## Flags

### Graph

-g, --graph  display graph of facts and rules nodes.

After reading the input file, first the rules, initial facts and queries are printed as read.
Then the facts are linked in a graph by parent and child rules.

For each fact node, the following is printed:
* initially true = True/False
* deduced true = True/False
* undetermined = True/False
* child rules: (list of rules)
* parent rules: (list of rules)

![Graph](https://github.com/dfinnis/expert-system/blob/master/img/graph.png?raw=true)

### Logic

-l, --logic  display reasoning, visualize logical steps taken.

This is a forward-chaining inference engine.
At first all rules with initalially true parents are added to the list of rules to be checked.
One at a time, each rule is checked.

If the antecedents are determined true, the consequents are deduced true.
Importantly, all rules with the newly deduced true facts as parents are now added to the list of rules to be checked.
This ensures logical truth is propogated through the graph, and rules are re-evaluated if their antecedent facts are updated as deduced true.
This rule applying loop runs until all rules necessary have been checked, and the truth of all facts has been determined.

![Logic](https://github.com/dfinnis/expert-system/blob/master/img/logic.png?raw=true)

#### Why forwards not backwards-chaining?

The implementation is simpler and more elegant, and the result is the same.
The only difference is the truth of all facts, not just the queried facts, is deduced.
