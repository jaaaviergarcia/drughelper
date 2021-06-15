import pandas as pd
import os
from datetime import datetime


from chembl_webresource_client.new_client import new_client
molecule = new_client.molecule

approved_drugs4 = molecule.filter(max_phase=4)
approved_drugs3 = molecule.filter(max_phase=3)
approved_drugs2 = molecule.filter(max_phase=2)
approved_drugs1 = molecule.filter(max_phase=1)

data = pd.DataFrame()


for i in range(len(approved_drugs4)):
    try:
        data = data.append({"Drug": approved_drugs4[i]['pref_name'], "Chemblid": approved_drugs4[i]['molecule_chembl_id'], "max_phase" : approved_drugs4[i]['max_phase'], "formula" : approved_drugs4[i]['molecule_properties']['full_molformula'] , "synonyms" : approved_drugs4[i]['molecule_synonyms'], "canonical" : approved_drugs4[i]['molecule_structures']['canonical_smiles']}, ignore_index = True)
    except:
        data = data.append({"Drug": approved_drugs4[i]['pref_name'], "Chemblid": approved_drugs4[i]['molecule_chembl_id'], "max_phase" : approved_drugs4[i]['max_phase'], "formula" : "-" , "synonyms" : approved_drugs4[i]['molecule_synonyms'], "canonical" : "-"}, ignore_index = True)

for i in range(len(approved_drugs3)):
    try:
        data = data.append({"Drug": approved_drugs3[i]['pref_name'], "Chemblid": approved_drugs3[i]['molecule_chembl_id'], "max_phase" : approved_drugs3[i]['max_phase'], "formula" : approved_drugs3[i]['molecule_properties']['full_molformula'] , "synonyms" : approved_drugs3[i]['molecule_synonyms'], "canonical" : approved_drugs3[i]['molecule_structures']['canonical_smiles']}, ignore_index = True)
    except:
        data = data.append({"Drug": approved_drugs3[i]['pref_name'], "Chemblid": approved_drugs3[i]['molecule_chembl_id'], "max_phase" : approved_drugs3[i]['max_phase'], "formula" : "-" , "synonyms" : approved_drugs3[i]['molecule_synonyms'], "canonical" : "-"}, ignore_index = True)

for i in range(len(approved_drugs2)):
    try:
        data = data.append({"Drug": approved_drugs2[i]['pref_name'], "Chemblid": approved_drugs2[i]['molecule_chembl_id'], "max_phase" : approved_drugs2[i]['max_phase'], "formula" : approved_drugs2[i]['molecule_properties']['full_molformula'] , "synonyms" : approved_drugs2[i]['molecule_synonyms'], "canonical" : approved_drugs2[i]['molecule_structures']['canonical_smiles']}, ignore_index = True)
    except:
        data = data.append({"Drug": approved_drugs2[i]['pref_name'], "Chemblid": approved_drugs2[i]['molecule_chembl_id'], "max_phase" : approved_drugs2[i]['max_phase'], "formula" : "-" , "synonyms" : approved_drugs2[i]['molecule_synonyms'], "canonical" : "-"}, ignore_index = True)

for i in range(len(approved_drugs1)):
    try:
        data = data.append({"Drug": approved_drugs1[i]['pref_name'], "Chemblid": approved_drugs1[i]['molecule_chembl_id'], "max_phase" : approved_drugs1[i]['max_phase'], "formula" : approved_drugs1[i]['molecule_properties']['full_molformula'] , "synonyms" : approved_drugs1[i]['molecule_synonyms'], "canonical" : approved_drugs1[i]['molecule_structures']['canonical_smiles']}, ignore_index = True)
    except:
        data = data.append({"Drug": approved_drugs1[i]['pref_name'], "Chemblid": approved_drugs1[i]['molecule_chembl_id'], "max_phase" : approved_drugs1[i]['max_phase'], "formula" : "-" , "synonyms" : approved_drugs1[i]['molecule_synonyms'], "canonical" : "-"}, ignore_index = True)

        
d =[]
for i in range(len(data['synonyms'])):
    for j in range(len(data['synonyms'][i])):
         d.append(data['synonyms'][i][j]['molecule_synonym'])
    
    data['synonyms'][i] = ";;;".join(d)
    d = []
    

nrows_old = 9021
nrows_new = 9020

date = datetime.now()
year = date.year
month = date.month
day = date.day


file = open("log.txt", "a")

if (nrows_new - nrows_old > 0): 
    
    newdrugs = nrows_new - nrows_old
    file.write("{}".format(year) + "{}".format(month) + "{}".format(day) + " : " + "{}".format(newdrugs) + " new drugs" + os.linesep)
    file.close()
    data.to_csv('dhdrugs.tsv', sep = '\t', index=False)
    
elif (nrows_new == nrows_old):
    
    file.write("{}".format(year) + "{}".format(month) + "{}".format(day) + " : " + "No changes" + os.linesep)
    file.close()
