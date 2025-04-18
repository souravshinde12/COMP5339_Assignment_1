from data_retrieval import *
from data_integration import *
import pandas as pd

# Main Function -
def main():
    #Step 1: Retrieving the data
    fuelcheck_raw_data = retrieve_fuelcheck_monthly_data() #Calling Retrivel Function 
    print("Raw Data", fuelcheck_raw_data)
    test_retrieve_fuelcheck_monthly_data(fuelcheck_raw_data) #Calling Test Function

    #Step 2: Data Cleaning
    fuelcheck_clean_data = data_cleaning(fuelcheck_raw_data) #Calling Data Cleaning Function

    #Save the cleaned data to CSV
    convert_cleaned_data_to_csv(fuelcheck_clean_data) #Calling Convert Function

pd.reset_option('display.max_columns')

main() 