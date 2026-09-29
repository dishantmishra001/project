## Project Statement

## Problem statement

Rolling dice manually can be inconvenient when a user wants to roll multiple dice or calculate their total. A simple command-line based system is needed to simulate dice rolls in an easy and interactive way.

The **Dice Rolling Simulator** is a Python based application that allows the user to enter the number of dice they want to roll. It generates random values from 1 to 6, displays the dice using simple ASCII art, calculates the total, and gives the user an option to roll again.

## Scope of the Project

The project focuses on developing a simple, interactive dice rolling simulator that runs through the command line.

The scope includes:

- Asking the user for the number of dice.
- Generating a random value from 1 to 6 for each die.
- Displaying the rolled dice using ASCII art.
- Calculating and displaying the total of all dice.
- Providing an option to roll the dice again.
- Allowing the user to exit the application.
- Handling invalid yes/no input when the user is asked whether to roll again.

The current version runs in the terminal and stores dice values temporarily in memory. Database storage, user accounts, graphical interfaces, and permanent data storage are outside the scope of the current version.

## Target Users

The primary target users are:

- **Students** - for learning and practicing basic Python programming concepts.
- **Beginners in Python** - for understanding lists, dictionaries, loops, functions/modules, user input, random numbers, and basic calculations.
- **Teachers/Faculty** - for demonstrating a simple Python command-line project.
- **Academic project evaluators** - for evaluating the implementation of a basic interactive Python application.

## High-Level Features

### 1. Enter Number of Dice
Allows the user to enter how many dice they want to roll.

### 2. Random Dice Roll
Generates a random number from 1 to 6 for every die.

### 3. Display Dice
Displays each rolled die using ASCII-art designs.

### 4. Calculate Total
Adds the values of all rolled dice and displays the total.

### 5. Roll Again
Allows the user to roll the dice again by entering `y`.

### 6. Exit
Allows the user to stop the program by entering `n`.

### 7. Input Validation
Displays an appropriate message when the user enters an invalid response for the roll-again option.

### 8. Command-line Execution
The application is designed to run directly in a terminal or command prompt without requiring a graphical user interface.

### 9. In-Memory Data Management
Uses a Python list to temporarily store the dice values while the program is running.
