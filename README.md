# Dictionary_Algebra

## Overview

**Dictionary_Algebra** is a Python program that treats a dictionary as a mathematical object and analyzes its structural properties using graph-theoretic and algebraic tools. Words are represented as nodes in a directed graph, with edges indicating definitional dependencies. The project investigates foundational questions such as:

- Can every word be defined from a given subset of words?
- Does the dictionary contain circular definitions?
- What are the minimal sets of words required to define the rest?
- Can the dictionary be decomposed into independently definable components?

## Features

- Parses dictionaries stored as Python dictionaries (mapping words to their definitions).
- Builds directed graphs where words point to the words they depend on for their definition.
- Identifies:
  - Cycles (circular definitions).
  - Definitional closure (which words can be reached from a given set).
  - Minimal defining sets.
  - Independent subdictionaries (algebraic decomposition).
- Offers a mathematically rigorous but intuitive way of understanding definitional systems.

## Use Cases

- Educational tool for understanding definability and recursion.
- Linguistic and philosophical analysis of lexical systems.
- Experimental logic and AI foundations research.
- Demonstration of recursive graph algorithms in Python.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

Clone the repository:


git clone https://github.com/yourusername/Dictionary_Algebra.git
cd Dictionary_Algebra
Running the Code
The main script can be run as:


python dictionary_algebra.py
Modify the dictionary variable within the script or import external dictionaries as needed.

Example Dictionary Format

dictionary = {
    "apple": "a fruit",
    "fruit": "a food that grows on trees",
    "food": "something you eat"
}
File Structure
dictionary_algebra.py — Main analysis code.

example_dictionary.py (optional) — A sample dictionary you can test with.

README.md — Project documentation.

Contributions
Contributions, suggestions, and pull requests are welcome! Feel free to fork the repo and submit improvements.

License
MIT License

Author
Billy McCarthy
