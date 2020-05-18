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


def main():
    print("CSV de muestras \"sequences.csv\" actualizado a día /05/2020.\n")
    print("¿Que tipo de ejecución deseas hacer?\n")
    print("\tEjecución Tipo 1 - Local Execution:\n"
          "\t\t- Carga desde el archivo alignmets.csv el resultado si se hubiera ejecutado el needleman_wunsch.\n"
          "\t\tDamos esta opción para ahorrar tiempo\n")
    print("\tEjecución Tipo 2 - External Execution:\n"
          "\t\t- Genera nuevos datos alignments maximum scores al ejecutar el algoritmo needleman_wunsch.\n")
    selection = input("¿Quieres ejecutar 1 o 2?\n")
    k = int(input("¿Cuántos clusters quieres generar?"))
    if "1" in selection:
        local_execution(k)
    else:
        external_execution(k)


def local_execution(k):
    # First the program obtains the median sample for each country.
    dictionary_median_accessions = m1.select_accessions()
    # In second place, the program associates the RNA
    dictionary_with_median_accessions = dictionary_median_accessions
    # sequence with the sample FASTA.
    dictionary_with_fasta = m2.fasta_rna(dictionary_with_median_accessions)
    # Load alignments maximum scores from a file
    alignment_scores_dictionary = m2.load_alignments(list(dictionary_with_fasta.keys()))
    # sequence with the sample distances between alignments, load alignments from local.
    distances_dictionary = m2.distances(alignment_scores_dictionary)
    # Clustering process.
    clusters = m3.clustering(distances_dictionary, k)
    print(clusters)
    print(pd.DataFrame(clusters).T)


def external_execution(k):
    # First the program obtains the median sample for each country.
    dictionary_median_accessions = m1.select_accessions()
    # In second place, the program associates the RNA
    dictionary_with_median_accessions = dictionary_median_accessions
    # sequence with the sample FASTA.
    dictionary_with_fasta = m2.fasta_rna(dictionary_with_median_accessions)
    # Calculate new alignments maximum scores with rust
    alignment_scores_dictionary = m2.create_dictionary(dictionary_with_fasta)
    # sequence with the sample distances between alignments, new calculate of alignments.
    distances_dictionary = m2.distances(alignment_scores_dictionary)
    # Clustering process.
    clusters = m3.clustering(distances_dictionary, k)
    print(clusters)
    print(pd.DataFrame(clusters).T)


if __name__ == '__main__':
    main()
