import csv


# Dado un csv se selecciona la muestra accesion median para cada pais.
def select_accessions():
    with open('sequences.csv', newline='') as csvfile:
        data = csv.DictReader(csvfile, delimiter=",")
        row = next(data)
        countries = dict()
        countries[row["Geo_Location"]] = dict()
        countries[row["Geo_Location"]]["Length"] = [int(row["Length"])]
        countries[row["Geo_Location"]]["Accession"] = [str(row["Accession"])]

        for row in data:
            location = row["Geo_Location"].split(":")[0]
            if location in list(countries.keys()):
                countries[location]["Accession"].append(str(row["Accession"]))
                countries[location]["Length"].append(int(row["Length"]))
            else:
                countries[location] = dict()
                countries[location]["Length"] = [int(row["Length"])]
                countries[location]["Accession"] = [str(row["Accession"])]

        median_countries = dict()
        for x in list(countries.keys()):
            median_countries[x] = median(countries[x]["Length"], len(countries[x]["Length"])//2)
        return final_median_dict(countries, median_countries)


# Devuleve el valor mediano de una lista de valores
def median(values, n):
    pivot = values[0]
    below = [x for x in values if x < pivot]
    above = [x for x in values if x > pivot]

    num_less = len(below)
    num_lessoreq = len(values) - len(above)

    if n < num_less:
        return median(below, n)
    elif n >= num_lessoreq:
        return median(above, n - num_lessoreq)
    else:
        return pivot


# This function, once we get the median value of each country, it creates a dictionary that contains all the medians'
# Accessions related with their country.


def final_median_dict(countries, median_countries):
    result = dict()
    for x in list(countries.keys()):
        medianIn = countries[x]["Length"].index(median_countries[x])
        result[x] = dict()
        result[x].update({"Accession": countries[x]["Accession"][medianIn]})
    return result
