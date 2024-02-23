Curriculum
SE Foundations
Average: 96.23%
0x07. Python - Test-driven development
Python
UnitTests
TDD
 By: Guillaume
 Weight: 1
 Project over - took place from Feb 8, 2024 3:00 AM to Feb 14, 2024 3:00 AM
 An auto review will be launched at the deadline
In a nutshell…
Auto QA review: 0.0/167 mandatory & 0.0/104 optional
Altogether:  0.0%
Mandatory: 0.0%
Optional: 0.0%
Calculation:  0.0% + (0.0% * 0.0%)  == 0.0%
Concepts
For this project, we expect you to look at this concept:

Never forget a test


Background Context
Important notice on intranet checks for Python projects
Starting from today:

Based on the requirements of each task, you should always write the documentation (module(s) + function(s)) and tests first, before you actually code anything
The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
We strongly encourage you to work together on test cases, so that you don’t miss any edge case. But not in the implementation of them!
Don’t trust the user, always think about all possible edge cases
Resources
Read or watch:

doctest — Test interactive Python examples (until “26.2.3.7. Warnings” included)
doctest – Testing through documentation
Unit Tests in Python
Unittest module
Interactive and Non-interactive tests
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
What’s an interactive test
Why tests are important
How to write Docstrings to create tests
How to write documentation for each module and function
What are the basic option flags to create tests
How to find edge cases
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
Python Test Cases
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
All your test files should be text files (extension: .txt)
All your tests should be executed by using this command: python3 -m doctest ./tests/*
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!
# Python - Test-driven development
In this project, I started practicing test-driven development using `docstring`
and `unittest` in Python.

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. Includes both Holberton-provided ones as well as the
following eight independently-developed:
  * [0-add_integer.txt](./tests/0-add_integer.txt)
  * [2-matrix_divided.txt](./tests/2-matrix_divided.txt)
  * [3-say_my_name.txt](./tests/3-say_my_name.txt)
  * [4-print_square.txt](./tests/4-print_square.txt)
  * [5-text_indentation.txt](./tests/text_indentation.txt)
  * [6-max_integer_test.py](./tests/6-max_integer_test.py)
  * [100-matrix_mul.txt](./tests/100-matrix_mul.txt)
  * [101-lazy_matrix_mul.txt](./tests/101-lazy_matrix_mul.txt)

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                     | Prototype                                    |
| ------------------------ | -------------------------------------------- |
| `0-add_integer.py`       | `def add_integer(a, b=98):`                  |
| `2-matrix_divided.py`    | `def matrix_divided(matrix, div):`           |
| `3-say_my_name.py`       | `def say_my_name(first_name, last_name=""):` |
| `4-print_square.py`      | `def print_square(size):`                    |
| `5-text_indentation.py`  | `def text_indentation(text):`                |
| `100-matrix_mul.py`      | `def matrix_mul(m_a, m_b):`                  |
| `101-lazy_matrix_mul.py` | `def lazy_matrix_mul(m_a, m_b):`             |
| `102-python.c`           | `void print_python_string(PyObject *p);`     |

## Tasks :page_with_curl:

* **0. Integers addition**
  * [0-add_integer.py](./0-add_integer.py): Python function that returns the integer addition
  of two numbers.
  * If either of `a` or `b` is not an `int` or `float`, a `TypeError` is raised
  with the message `a must be an integer` or `b must be an integer`.
  * If either of `a` or `b` is a `float`, it is casted to an `int`
  before addition.

* **1. Divide a matrix**
  * [2-matrix_divided.py](./2-matrix_divided.py): Python function that divides all
  elements of a matrix by a common divisor.
  * Returns a new matrix representing the division of all elements of `matrix`
  by `div`.
  * Quotients are rounded to two decimal places.
  * If `matrix` is not a list of lists of `int`s or `float`s, a `TypeError`
  is raised with the message `matrix must be a matrix (list of lists) of
  integers/floats`.
  * If `matrix` contains rows of different lengths, a `TypeError` is raised
  with the message `Each row of the matrix must have the same size`.
  * If the divisor `div` is not an `int` or `float`, a `TypeError` is raised
  with the message `div must be a number`.
  * If `div` is `0`, a `ZeroDivisionError` is raised with the message
  `division by zero`.

* **2. Say my name**
  * [3-say_my_name.py](./3-say_my_name.py): Python function that prints a name in
  the format `My name is <first_name> <last_name>`.
  * If either of `first_name` or `last_name` is not a `str`, a `TypeError` is
  raised with the message `first_name must be a string` or `last_name must be a
  string`.

* **3. Print square**
  * [4-print_square.py](./4-print_square.py): Python function that prints a square using
  the `#` character.
  * The paramter `size` represents the height/width of the square.
  * If `size` is not an `int`, a `TypeError` is raised  with the message,
  `size must be an integer`.
  * If `size` is less than `0`, a `ValueError` is raised with the message `size
  must be >= 0`.

* **4. Text indentation**
  * [5-text_indentation.py](./5-text_indentation.py): Python function that prints text with
  indentation.
  * Two new lines are printed after any `.`, `?`, or `:` character.
  * If `text` is not a `str`, a `TypeError` is raised with the message `text
  must be a string`.
  * No spaces are printed at the beginning or end of each printed line.

* **5. Max integer - Unittest**
  * [tests/6-max_integer_test.py](./tests/6-max_integer_text.py): Python class/script
  that runs unittests for the function `def max_integer(list=[]):`
  (provided by Holberton School).

* **6. Matrix multiplication**
  * [100-matrix_mul.py](./100-matrix_mul.py): Python function that multiplies two matrices.
  * Returns a new matrix representing the multiplication of `m_a` by `m_b`.
  * If either of `m_a` or `m_b` is empty (ie. `== []` or `== [[]]`), a
  `ValueError` is raised with the message `m_a can't be empty` or `m_b can't
  be empty`.
  * If either of `m_a` or `m_b` is not a list, a `TypeError` is raised with
  the message `m_a must be a list` or `m_b` must be a list.
  * If either of `m_a` or `m_b` is not a list of lists, a `TypeError` is raised
  with the message `m_a must be a list of lists` or `m_b must be a list of lists`.
  * If either of `m_a` or `m_b` is not a list of lists of `int`s or `float`s, a
  `TypeError` is raised with the message `m_a should contain only integers or
  floats` or `m_b should contain only integers or floats`.
  * If either of `m_a` or `m_b` contains rows of different lengths, a `TypeError`
  is raised with the message `each row of m_a must should be of the same size` or
  `each row of m_b must should be of the same size`.
  * If `m_a` and `m_b` cannot be multiplied (ie. row size of `m_a` does not match
  column size of `m_b`), a `ValueError` is raised with the message `m_a and m_b
  can't be multiplied`.

* **7. Lazy matrix multiplication**
  * [101-lazy_matrix_mul.py](./101-lazy_matrix_mul.py): Python function that multiplies
  two matrices using the module `NumPy`.
  * Identical in function to [100-matrix_mul.py](./100-matrix_mul.py).

* **8. CPython #3: Python Strings**
  * [102-python.c](./102-python.c): C function that prints basic information about Python
  string objects.
