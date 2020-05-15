import pandas as pd
import module1 as m1
import module2 as m2


# First the program obtains the median sample for each country.
dictionary_median_accessions = m1.select_accessions()
# In second place, the program associates the RNA
dictionary_with_median_accessions = dictionary_median_accessions
# sequence with the sample FASTA.
dictionary_with_fasta = m2.fasta_rna(dictionary_with_median_accessions)
# sequence with the sample aligments.
result = m2.create_dictionary(dictionary_with_fasta)
print(pd.DataFrame(result).T)
# sequence with the sample distances bettween aligments.
# distances_dictionary = distances(load_aligments(list(dictionary_with_fasta.keys())))
# print(pd.DataFrame(distances_dictionary))
