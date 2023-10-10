'''
Project: 5.14 Project 6: Binary Search Tree
Author: Brock Terry
Course: CS 2420 X01
Date: 3-6-2023

Description:

This program creates a Binary Search Tree (BST) from an input text file. 
Each node in the BST contains a 'Pair' object which represents a letter 
from the text and the count of its occurrences. The program excludes whitespace and punctuation 
from the input text. It demonstrates the use of a BST for storing and retrieving data in a sorted manner. 
It uses in-order traversal to print all the letters in the text along with their counts in alphabetical order.


Lessons Learned:

1. Learned how to implement a BST in Python, including the insertion and in-order traversal operations.
2. Learned about encapsulating related data into a single object (Pair) and using these objects as nodes in a BST.
3. Reinforced understanding of Python's magic methods by implementing comparison operators for the Pair class.
4. Learned about file handling in Python - reading a text file and processing its content.
5. Gained experience in using Python's string manipulation functions, such as checking if a character is whitespace or punctuation.

'''
from pathlib import Path
from string import whitespace, punctuation
from bst import BST

class Pair:
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count

    def __eq__(self, other):
        return self.letter == other.letter

    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'

    def __str__(self):
        return f'({self.letter}, {self.count})'

def make_tree():
    tree = BST()
    file_path = Path('around-the-world-in-80-days-3.txt')

    with open(file_path, 'r') as file:
        while True:
            char = file.read(1)
            if not char:
                break
            char = char.lower()
            if char not in whitespace + punctuation:
                try:
                    found = tree.find(Pair(char))
                    found.count += 1
                except ValueError:
                    tree.add(Pair(char))
    return tree

def main():
    tree = make_tree()

    print("Inorder Traversal:")
    print(tree.inorder())

    print("Preorder Traversal:")
    print(tree.preorder())

    print("Postorder Traversal:")
    print(tree.postorder())

def test_find():
    tree = BST()
    tree.add(10)
    tree.add(20)
    tree.add(30)
    try:
        tree.find(40)  # This should raise a ValueError
        print("Test failed: find method did not raise a ValueError.")
    except ValueError:
        print("Test passed: find method raised a ValueError as expected.")

if __name__ == "__main__":
    test_find()
    main()