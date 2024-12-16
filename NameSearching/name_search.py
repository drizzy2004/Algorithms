import numpy as np 
import argparse
import string

class NameSearch:

    def __init__(self, Name_List, Name_Algorithm, Name_Length):
        # Matrix of the word search puzzle 
        self.matrix = np.load("./data/matrix.npy")
        # Name of the algorithm
        self.Name_Algorithm = Name_Algorithm
        # Length of the name
        self.Name_Length = Name_Length
        # List of all potential names 
        with open("./data/names/"+Name_List+".txt", 'r') as f:
            self.names = f.read().splitlines()
        self.names = [n.upper().strip() for n in self.names]

        self.rows, self.cols = self.matrix.shape
        self.table = dict.fromkeys(string.ascii_uppercase, 0)

    def match_BruteForce(self, pattern, text):
        # String matching by brute force
        index = 0
        for letter in text:
            if letter == pattern[index]:
                index += 1
            else:
                index = 0

            if index == len(pattern):
                print(f"The name is {pattern}!")
                break


    def match_Horspool(self, pattern, text):
        # String matching by Horspool's algorithm
        table_length = len(self.table)
        pattern_length = len(pattern)

        for i in range(0, table_length):
            self.table[chr(i + 65)] = pattern_length

            for j in range(0, pattern_length - 1):
                self.table[pattern[j]] = pattern_length - 1 - j

        index = pattern_length - 1

        while index <= (len(text) - 1):
            letters = 0
            while letters <= pattern_length - 1 and pattern[pattern_length - 1 - letters] == text[index - letters]:
                letters += 1
            if letters == pattern_length:
                print(f"The name is {pattern}")
                return index - (pattern_length + 1)
            else:
                index += self.table[text[index]]
        return -1


    def get_row(self, matrix, row):
        text = ""
        for col in range(self.cols):
            text += matrix[row, col]
        return text

    def get_col(self, matrix, col):
        text = ""
        for row in range(self.rows):
            text += matrix[row, col]
        return text

    def get_left_diagonal(self, matrix):
        text = ""

        for diagonal in range(-(self.rows - 1), self.cols):
            x = max(0, -diagonal)
            y = max(0, diagonal)

            while x < self.rows and y < self.cols:
                text += matrix[x][y]
                x += 1
                y += 1

        return text

    def get_right_diagonal(self, matrix):
        text = ""

        for diagonal in range(self.rows + self.cols - 1):
            if diagonal < self.rows:
                x = 0
                y = diagonal
            else:
                y = self.cols - 1
                x = diagonal - y

            while x < self.rows and y >= 0:
                text += matrix[x][y]
                x += 1
                y -= 1

        return text


    def search(self):
        # pattern is each name in self.names
        # text is each horizontal, vertical, and diagonal strings in self.matrix

        for pattern in self.names:
            if len(pattern) == self.Name_Length:
                for row in range(self.rows):
                    text = self.get_row(self.matrix, row)
                    if self.Name_Algorithm == "BruteForce":
                        self.match_BruteForce(pattern, text)
                    elif self.Name_Algorithm == "Horspool":
                        self.match_Horspool(pattern, text)

                for col in range(self.cols):
                    text = self.get_col(self.matrix, col)
                    if self.Name_Algorithm == "BruteForce":
                        self.match_BruteForce(pattern, text)
                    elif self.Name_Algorithm == "Horspool":
                        self.match_Horspool(pattern, text)

                text = self.get_left_diagonal(self.matrix)
                if self.Name_Algorithm == "BruteForce":
                    self.match_BruteForce(pattern, text)
                elif self.Name_Algorithm == "Horspool":
                    self.match_Horspool(pattern, text)

                text = self.get_right_diagonal(self.matrix)
                if self.Name_Algorithm == "BruteForce":
                    self.match_BruteForce(pattern, text)
                elif self.Name_Algorithm == "Horspool":
                    self.match_Horspool(pattern, text)


if __name__ == "__main__":
        
    parser = argparse.ArgumentParser(description='Word Searching')
    parser.add_argument('-name', dest='Name_List', required = True, type = str, help='Name of name list')
    parser.add_argument('-algorithm', dest='Name_Algorithm', required = True, type = str, help='Name of algorithm')
    parser.add_argument('-length', dest='Name_Length', required = True, type = int, help='Length of the name')
    args = parser.parse_args()

    # Example:
    # python name_search.py -algorithm BruteForce -name Mexican -length 5

    obj = NameSearch(args.Name_List, args.Name_Algorithm, args.Name_Length)
    obj.search()


