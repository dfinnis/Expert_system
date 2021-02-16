# expert-system

An expert system for propositional calculus, written in python.

A forward-chaining inference engine.

Accepts a list of rules, facts, and queries. It applies logic, then for each query it prints True/False/Undetermined.

## Getting Started

Simply clone this repo.

### Usage

![Usage](https://github.com/dfinnis/expert-system/blob/master/img/usage.png?raw=true)

### input file formatting

```
# this is a comment, spacing is not important

A     => B    # Rule: A implies B
A + B => C    # Rule: A and B implies D

=A            # Initial facts: A is true

?B            # Queries: is B true?
```

### Logical operations

The following symbols are defined, in order of decreasing priority:

* ()    Parenthesis   Example: A + (B | C) => D
* \+    AND           Example: A + B
* |   # OR            Example: A | B
* ˆ   # XOR           Example: A ˆ B
* =>  # implies       Example: A + B => C

### Examples

### Dependencies

Python

## Tests

## Flags

## References


