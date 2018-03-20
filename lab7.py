# Programmers: Harrison Russo, Conor O'Brien
# Lab 7

import os

movieFile = input( "Please enter a file name > " )
while not os.path.exists( filename ):
    filename = input("Please enter a file name > ")

print( "1 - Thank you,", filename, "is a valid file name" )

try:
    filename = input( "Enter a file name > " )
    file_object = open( filename, "r" )
    print( "File successfully open for reading" )
except FileNotFoundError:
    print( "File does not exist" )

print( "2 - Thank you for trying to opne a file" )

filenameInvalid = True
while filenameInvalid:
    try:
        filename = input("Enter a file name > ")
        file_object = open(filename, "r")
        filenameInvalid = False
    except FileNotFoundError:
        print("File does not exist")

print( "3 - Thank you,", filename, "is open for reading" )