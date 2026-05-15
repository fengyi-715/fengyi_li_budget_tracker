# Final Project PRD

## Project Title

Python Personal Budget Tracker

## One Sentence Pitch

My project is a program that records personal income and expenses with amounts and purposes, calculates the daily available spending limit, and stores transaction history for easy review.

## Target User

This project is for high school students (like me) who want to track their pocket money, allowance, or part-time job income, and manage their daily spending to avoid overspending.

## Purpose

This is useful or interesting because it helps students develop good financial habits, keeps track of where their money goes, and uses practical Python skills to solve a real-life problem like managing personal finances.

## MVP

The smallest working version will be a text-based command-line program that allows users to add income/expense transactions, view transaction history, calculate the daily spending limit based on remaining balance and days left in the month, and save transaction data locally so records don't disappear when the program closes.

## Must Have Features

1. Add Transaction - Input transaction type (income/expense), amount, and purpose, with error handling for invalid inputs.
2. View Transaction History - Display all recorded transactions clearly, including type, amount, purpose, and date.
3. Calculate Daily Spending Limit - Compute daily available money by dividing remaining balance by days left in the month.

## Nice To Have Features

1. Transaction Categorization - Add categories to transactions and view spending by category.
2. Monthly Summary - Generate a summary of total income, total expenses, and net balance for the month.

## Stretch Feature

1. Basic Spending Chart - Use a simple library to create a bar chart showing monthly spending by category.

## Python Skills I Might Use

### Functions
Reusable functions for adding transactions, viewing history, calculating daily limits, and handling file operations.

### Lists
Store all transactions in a list to easily iterate through and display the full history.

### Dictionaries
Store each transaction as a dictionary with keys (type, amount, purpose, date) to organize related data.

### APIs
Not required for MVP; may be used for stretch feature if needed.

### File I/O
Read or write transaction data to a .txt or .csv file to save records between program sessions.

### OOP
Create Transaction and BudgetTracker classes to encapsulate transaction data and core program functions.

### Error Handling
Use try/except blocks to handle invalid inputs, non-numeric amounts, and missing data files.

## Data Plan

**What data does my project need?**
Transaction type, amount, purpose, date; total balance; days left in the month.

**Where will the data come from?**
User input and system-generated data.

**How will I store or organize the data?**
In-memory list of dictionaries for active use; save to a .txt/.csv file for persistence.

## First Tiny Step

The first thing I need to build is a function that collects transaction type, amount, and purpose, stores it as a dictionary in a list, and prints the list to confirm it works.

## Possible Risk

The hardest part might be implementing file reading or writing and calculating days left in the month.
