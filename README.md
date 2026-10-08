# Bookbot

A command-line Python program that analyzes a book's text file and reports its total word count and how often each letter appears, sorted from most to least common.

Built as a guided project in Boot.dev's Backend Developer path. It was my first Python project built and run on my own machine.

## What it does

- Counts the total number of words in a book
- Counts every character (uppercase and lowercase treated as the same)
- Sorts letters from most to least common and prints a clean report

## How to run

Requires Python 3.

```
git clone https://github.com/T-McMann/bookbot.git
cd bookbot
python3 main.py books/frankenstein.txt
```

Works with any plain `.txt` file: `python3 main.py path/to/your/book.txt`

## Example output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
...
============= END ===============
```

## What I learned

- Reading files and working with text in Python
- Counting things with dictionaries
- Sorting data with a custom sort function
- Splitting code across multiple files with imports
- Taking input from the command line with `sys.argv`
- Working in the Linux terminal and debugging from error messages
