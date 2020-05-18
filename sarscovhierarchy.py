"""
    pandas: Biblioteca que nos sirve para imprimir diccionarios en forma de tabla.
    module1: Importa las funciones referentes a la primera parte de la práctica (Accessions)
    module2: Importa las funciones referentes a la segunda parte de la práctica (calcular aligments)
    module3: Importa las funciones referentes a la tercera parte de la práctica ()
"""
import pandas as pd
import module1 as m1
import module2 as m2
import module3 as m3

# First the program obtains the median sample for each country.
dictionary_median_accessions = m1.select_accessions()
# In second place, the program associates the RNA
dictionary_with_median_accessions = dictionary_median_accessions
# sequence with the sample FASTA.
dictionary_with_fasta = m2.fasta_rna(dictionary_with_median_accessions)
# sequence with the sample alignments.
#result = m2.create_dictionary(dictionary_with_fasta)
# sequence with the sample distances between alignments.
distances_dictionary = m2.distances(m2.load_alignments(list(dictionary_with_fasta.keys())))
clusters = m3.clustering(distances_dictionary, 12)
print(clusters)
print(pd.DataFrame(clusters).T)
