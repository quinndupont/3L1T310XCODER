

# Import necessary libraries
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

# Define function to calculate percentage difference
def calculate_percentage_difference(current_value, record_high):
    """
    Calculates the percentage difference between the current value and the record high.
    Inputs:
        current_value: float, representing the current value of a stock or asset
        record_high: float, representing the record high of the stock or asset
    Returns:
        percentage_difference: float, representing the percentage difference between current value and record high
    """
    percentage_difference = 100 * (current_value - record_high) / record_high
    return percentage_difference

# Define function to prompt user for current price and record highs of assets
def get_input():
    """
    Prompts user to input the current price of Bitcoin, as well as the record highs of Gold and the S&P 500.
    Returns:
        btc_price: float, representing the current price of Bitcoin
        gold_record_high: float, representing the record high of Gold
        sp500_record_high: float, representing the record high of the S&P 500
    """
    btc_price = float(input("Enter the current price