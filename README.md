# expert-system

An expert system for propositional calculus, written in python.

A forward-chaining inference engine.

Accepts a list of rules, facts, and queries. It applies logic, then for each query it prints True/False/Undetermined.

## Getting Started

Simply clone this repo.

### Usage

Run with input filepath as argument

![Usage](https://github.com/dfinnis/expert-system/blob/master/img/usage.png?raw=true)

### input file formatting

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

### Dependencies

Python

## Tests

The test script runs input files from the ```input``` folder, and ensures the output is correct.

Tests are grouped into and, or, xor, not, same conclusion, parenthesis and error tests.

![Tests](https://github.com/dfinnis/expert-system/blob/master/img/tests.gif)

## Flags

## References


