"""
This script processes EU Pfizer vaccine data, extracts symptoms, and generates
a bar plot of the top 20 reported symptoms.
"""
import glob  # Standard import
import re  # Standard import
import pandas as pd
import graphs as gp


# Merging all the EU data files
def clean(data_frame):
    """
    Cleans the data for EU Pfizer vaccine reports.

    Parameters:
    data_frame (pd.DataFrame): DataFrame containing EU Pfizer vaccine data.

    Returns:
    pd.DataFrame: Cleaned DataFrame.
    """

    def extract_symptoms(symptom_list):
        """
        Extracts symptoms from the symptom list.

        Parameters:
        symptom_list (str): String containing symptoms separated by <BR><BR> tags.

        Returns:
        list: List of symptoms.
        """
        if isinstance(symptom_list, str):
            symptoms = re.split(r'<BR><BR>', symptom_list)
            symptoms = [re.split(r'\(', symptom.strip())[0].strip() for symptom in symptoms]
            return symptoms
        return []
    # Renaming the columns
    data_frame.columns = ["EU_ID", "1", "2", "3", "4", "5", "AGE_GROUP",
                              "6", "7", "SEX", "SYMPTOMS_LIST", "8", "9", "10"]
    # Selection of specific columns
    data_frame = data_frame[["EU_ID", "AGE_GROUP", "SEX", "SYMPTOMS_LIST"]]
    # Applying the function to the symptom list column to extract the specific symptoms
    data_frame["SYMPTOMS_LIST"] = data_frame["SYMPTOMS_LIST"].apply(extract_symptoms)
    # Renaming the age group column
    data_frame["AGE_GROUP"] = data_frame["AGE_GROUP"].astype(str).str.replace(
        "Years", ""
    ).str.strip()
    # Renaming the sex column
    data_frame["SEX"] = data_frame["SEX"].astype(str).str.replace("emale", "F").str.strip()
    data_frame["SEX"] = data_frame["SEX"].astype(str).str.replace("ale", "M").str.strip()
    data_frame["SEX"] = data_frame["SEX"].astype(str).str.replace(
        "Not Specified", "U"
    ).str.strip()
    # Renaming the VAX_MANU column to Pfizer
    data_frame['VAX_MANU'] = "PFIZER"
    return data_frame


if __name__ == '__main__':
    data_eu_pfizer = pd.DataFrame()
    for file_name in glob.glob('EU Files/EU PFIZER' + '*.csv'):
        x = pd.read_csv(file_name, low_memory=False)
        data_eu_pfizer = pd.concat([data_eu_pfizer, x], axis=0, ignore_index=True)
    clean_data= clean(data_eu_pfizer)
    clean_data.to_csv("output_files/eu_output.csv")

    # Creating a bar plot of the number of symptoms by Pfizer vaccine in EU
    eu_output = pd.read_csv("/Users/adi/Desktop/MS1/git/output_files/eu_output.csv")
    plot = gp.symptom_by_vax_manu(eu_output)

    # Save the plot
    plot.savefig('/Users/adi/Desktop/MS1/git/output_files/symptoms_by_pfizer_barplot.png')
