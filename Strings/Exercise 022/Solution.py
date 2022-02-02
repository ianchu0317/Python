#!/usr/bin/bash

def sort_key(char):
    return char

if __name__ == '__main__':
    print("".join(sorted(input("Enter a string: "), key=sort_key)))
