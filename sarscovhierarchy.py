import csv
with open('sequences.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile, delimiter=";")
    first_row = next(data)
    location = first_row["Geo_Location"]
    countries = {}
    countries[location] = list()
    countries[location].append(first_row["Length"])
    for row in data:
        if location in row["Geo_Location"]:
            countries[location].append(row["Length"])
        else:
            location = row["Geo_Location"]
            countries[location] = list()
            countries[location].append(first_row["Length"])
    print(countries)