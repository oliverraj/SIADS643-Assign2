"""
This file is used for generating final graphs
for the analysis of the project. There are functions
that when called generate a plot.
"""
# Importing the required libraries.
import matplotlib.pyplot as plt
import seaborn as sns
def symptom_by_vax_manu(data_eu):
    """
    This file is used for generating final graphs
    for the analysis of the project. There are functions
    that when called generate a plot.

    **symptom_by_vax_manu** function generates a bar chart showing the top 
    20 most frequent symptoms reported for the Pfizer vaccine in the EU data.
    Parameters:
    data_eu (pd.DataFrame): DataFrame containing the EU vaccination data.
    Returns:
    matplotlib.pyplot.Figure: The plot object representing the bar chart.
    """
# Importing the required libraries.
    all_symptoms = data_eu.explode(["SYMPTOMS_LIST"])
    eu_exploded = all_symptoms.dropna(subset=['SYMPTOMS_LIST'])
    pfizer_symptoms = eu_exploded[eu_exploded['VAX_MANU'] == 'PFIZER']
    reaction_counts1 = pfizer_symptoms['SYMPTOMS_LIST'].value_counts()
    reaction_counts_df = reaction_counts1.reset_index()
    reaction_counts_df.columns = ['Symptom', 'Count']
    top_20_sym_pfizer = reaction_counts_df.head(20)
    plt.figure(figsize=(12, 8))
    # Create the bar plot
    sns.barplot(
    x='Count',
    y='Symptom',
    data=top_20_sym_pfizer.sort_values('Count', ascending=False),
    palette='viridis',
    hue='Symptom',
    dodge=False,
    legend=False
)
    plt.xlabel('Count')
    plt.ylabel('Symptom')
    plt.title('Top 20 Reported Symptoms of Pfizer in EU')
    return plt
