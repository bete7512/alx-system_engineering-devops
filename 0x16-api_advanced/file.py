#!/usr/bin/python3
import sys
def search_str(file_path, word):
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:
            print('string exist in a file')
        else:
            print('string does not exist in a file')

search_str(r'./test.txt', 'laptop')