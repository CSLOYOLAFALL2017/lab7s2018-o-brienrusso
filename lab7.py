# Programmers: Harrison Russo, Conor O'Brien
# Prof. Franceschi
# Spring 2018 CS 151.02
# Lab 7

# Import the frameworks
import os
import sys

# Define the function to determine if the inputted file is valid
def validFile():
    movieFile = input("Please enter a file name: ")
    while not os.path.exists(movieFile):
        movieFile = input("Please enter a file name: ")
    return movieFile

# Define the function to open the file and calculate the profit for each movie
def profit(openFile):
    # Ensure the file exists
    try:
        # Open the file for reading
        openFile = open(openFile, "r")
        # Set the maxProfit = 0 before checking the file, and the maxProfitMovie to an empty string
        maxProfit = 0
        maxProfitMovie = ""
        # Check each line in the file for the profit
        for line in openFile:
            # Store the following data in their respective variables from the line in the file
            releaseDate, movieTitle, budget, boxOffice = line.split(",")
            # Convert budget and boxOffice to floats so they can be calculated
            budget = float(budget)
            boxOffice = float(boxOffice)
            # Calculate the revenue
            revenue = boxOffice - budget
            # If the movie's revenue is greater than the max profit, it will become the new max profit
            if revenue > maxProfit:
                # Set the maxProfit to equal the revenue from the movie
                maxProfit = revenue
                # Store the name of the movie with the most profit so far
                maxProfitMovie = movieTitle
    except FileNotFoundError:
        # If the file is not found output the following text before closing the app
        print("Sorry this file does not exist")
        sys.exit()

    # Output the movie with the highest profit
    print("The movie with the most profit is:", maxProfitMovie, "with a profit of $%.2f" % maxProfit)
    return

# Define the function to output data to the file
def output(openFile, outputFile):
    # Open the file for writing
    newOutputFile = open(outputFile,"w")
    # Check that the file exist
    try:
        openFile = open(openFile, "r")
        # Check each line in the input file and output them to the output file
        for line in openFile:
            # Store the following data in their respective variables
            releaseDate, movieTitle, budget, boxOffice = line.split(",")
            # Convert the following variables to floats so they can be calculated
            budget = float(budget)
            boxOffice = float(boxOffice)
            # Calculate the revenue
            revenue = boxOffice - budget
            # Print the release date, movie title, and revenue to the file that the user inputted
            print("Release date:", releaseDate, file=newOutputFile)
            print("Movie title:", movieTitle, file=newOutputFile)
            print("Revenue: $%.2f" % revenue, file=newOutputFile)
            # White space between each line in the output file
            print(" ", file=newOutputFile)
    except FileNotFoundError:
        print("Sorry this file does not exist")
        sys.exit()
    return

def main():
    print("The purpose of this program is to output the movie with the highest profit from a list you input.")
    # Call the valid input file function
    openFile = validFile()
    # Call the output file function
    outputFile = input("Enter a file to output to: ")

    # Call the profit function
    profit(openFile)
    # Call the output function
    output(openFile, outputFile)

    return

# Call the main function
main()
