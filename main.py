#Importing all the librries
import pandas as pd
import glob
import matplotlib.pyplot as plt 
import seaborn as sns
import os
import re
#"Merging all the US data files"
def clean(data_EU_pfizer):
    def extract_symptoms(symptom_list):

        if isinstance(symptom_list, str):
            # Split the reactions using the HTML break tag as the delimiter
            symptoms = re.split(r'<BR><BR>', symptom_list)
            # Further clean and extract just the reaction name before the first parenthesis
            symptoms = [re.split(r'\(', symptom.strip())[0].strip() for symptom in symptoms]
            return symptoms
        else:
            return []
            
    data_EU_pfizer.columns = ["EU_ID", "1", "2", "3", "4", "5", "AGE_GROUP", "6", "7", "SEX", "SYMPTOMS_LIST", "8", "9", "10"]
    data_EU_pfizer = data_EU_pfizer[["EU_ID", "AGE_GROUP", "SEX", "SYMPTOMS_LIST"]]
        # data_EU_pfizer.head(2)
    data_EU_pfizer["SYMPTOMS_LIST"] = data_EU_pfizer["SYMPTOMS_LIST"].apply(extract_symptoms)
        # data_EU_pfizer
    data_EU_pfizer["AGE_GROUP"] = data_EU_pfizer["AGE_GROUP"].astype(str).str.replace("Years", "").str.strip()
        # data_EU_pfizer
    data_EU_pfizer["SEX"] = data_EU_pfizer["SEX"].astype(str).str.replace("emale", "").str.strip()
    data_EU_pfizer["SEX"] = data_EU_pfizer["SEX"].astype(str).str.replace("ale", "").str.strip()
    data_EU_pfizer["SEX"] = data_EU_pfizer["SEX"].astype(str).str.replace("Not Specified", "U").str.strip()
    # data_EU_pfizer
    data_EU_pfizer['VAX_MANU'] = "PFIZER"
    return data_EU_pfizer
if __name__ == '__main__':
    data_EU_pfizer = pd.DataFrame()
    for file_name in glob.glob('EU Files/EU PFIZER' + '*.csv'):
        x = pd.read_csv(file_name, low_memory = False)
        data_EU_pfizer = pd.concat([data_EU_pfizer, x], axis = 0, ignore_index = True)      
    data = clean(data_EU_pfizer)
    data.to_csv("output_files/eu_output.csv")
  
