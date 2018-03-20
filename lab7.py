# Programmers: Harrison Russo, Conor O'Brien
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
        openFile = open(openFile, "r")
        # Set the maxProfit = 0 before checking the file
        maxProfit = 0
        maxProfitMovie = ""
        # Check each line in the file for the profit
        for line in openFile:
            releaseDate, movieTitle, budget, boxOffice = line.split(",")
            # Convert budget and boxOffice so they can be calculated
            budget = float(budget)
            boxOffice = float(boxOffice)
            # Calculate the revenue
            revenue = boxOffice - budget
            # If the movie's revenue is greater than the max profit, it will become the new max profit
            if revenue > maxProfit:
                maxProfit = revenue
                maxProfitMovie = movieTitle
    except FileNotFoundError:
        print("Sorry this file does not exist")
        sys.exit()

    # Output the movie with the highest profit
    print("The movie with the most profit is:", maxProfitMovie, "with a profit of $%.2f" % maxProfit)
    return
# Define the function to output data to the file
def output(openFile, outputFile):
    newOutputFile = open(outputFile,"w")
    # Check that the file exist
    try:
        openFile = open(openFile, "r")
        # Check each line in the input file and output them to the output file
        for line in openFile:
            releaseDate, movieTitle, budget, boxOffice = line.split(",")
            budget = float(budget)
            boxOffice = float(boxOffice)
            revenue = boxOffice - budget
            print(newOutputFile)
            print("Release date:", releaseDate, file=newOutputFile)
            print("Movie title:", movieTitle, file=newOutputFile)
            print("Revenue: $%.2f" % revenue, file=newOutputFile)
            # White space between each line in the output file
            print(" ", file=outputFile)
    except FileNotFoundError:
        print("Sorry this file does not exist")
        sys.exit()
    return


def main():
    print("The purpose of this program is to output the movie with the highest profit from a list you input.")
    # Call the valid input file function
    openFile = validFile()
    # Call the output file function
    outputFile = input("Input a file to output to: ")

    # Call the profit function
    profit(openFile)
    # Call the output function
    output(openFile,outputFile)
    return

main()