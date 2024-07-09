# Python String and Sequence Tasks

This project contains three Python functions that perform various string and sequence operations.

## Tasks

### 1. Anagram Checker

Function that checks if a given string is an anagram.

- Input: A string
- Output: Boolean (True if the string is an anagram, False otherwise)

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.

### 2. Symbol Counter

Function that counts the occurrences of a specific symbol in a string.

- Input: 
  - A string
  - A symbol (character)
- Output: Integer (number of times the symbol appears in the string)

### 3. Fibonacci Sequence Generator

Function that generates a Fibonacci sequence of a given length.

- Input: An integer n
- Output: List of n Fibonacci numbers

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

## Usage

Each function can be used independently. Here are examples of how to call each function:

```python
# Anagram Checker
result = is_anagram("listen", "silent")
print(result)  # Should print: True

# Symbol Counter
count = count_symbol("hello world", "l")
print(count)  # Should print: 3

# Fibonacci Sequence Generator
fib_sequence = fibonacci_sequence(10)
print(fib_sequence)  # Should print: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]