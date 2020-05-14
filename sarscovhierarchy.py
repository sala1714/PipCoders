from module1 import *
from module2 import *
from module3 import *
import pandas as pd


dictionary_median_accessions = select_accessions()  # First the program obtains the median sample for each country.
dictionary_with_fasta = fasta_RNA(dictionary_median_accessions)  # In second place, the program associates the RNA sequence with the sample.

# createDictionary(dictionary_with_fasta)
distances_dictionary = distances(load_aligments(list(dictionary_with_fasta.keys())))
print(pd.DataFrame(distances_dictionary))





