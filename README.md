## SIADS 643 Week 2 Converting Jupyter Notebook to Script
### Description: This is a  readme file describing the files contained in this EU Files folder.
#### File Descriptions
### 1. EU PFIZER 2023.csv
#### This is the raw csv file with adverse effects detail from Europe.This csv file has following columns:
1. EU local number - Case number
2. Report type
3. EU Gateway Receipt Date
4. Primary Source Qualification
5. Primary Source Country
6. Literature Reference
7. Patient Age Group
8. Patient Age Group (as per reporter)
9. Parent Child Report
10. Patient Sex
11. Reaction List
12. Suspect/interacting Drug List
13. Concomitant/Not Administered Drug List
14. ICSR Form
### 2. eu_output.csv
Many of the columns in the raw csv file were renamed and dropped. In addition, some of the columns were renamed. Ultimately, these columns were retained in the csv file for final analysis:
1. EU_ID - EU local number renamed
2. Age_group - Patient Age Group renamed
3. Sex - Patient Sex renamed
4. Symptoms_list - List of symptoms taken from reaction list
5. VAX_MANU - Vaccine manufacturer
