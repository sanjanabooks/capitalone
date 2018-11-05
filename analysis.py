import csv
import pandas as pd
from collections import Counter
import math
import numpy

df = pd.read_csv('metro-bike-share-trip-data.csv')

# most popular stations
start_id = Counter(list(df["Starting Station ID"]))
end_id = Counter(list(df["Ending Station ID"]))
final_start = (start_id.most_common(1))
final_end = (end_id.most_common(1))

# avg distance
df["Test"] = df["Starting Station Latitude"] - df["Ending Station Latitude"]
print(df["Test"])
df["Distance"] = ((df["Starting Station Latitude"] - df["Ending Station Latitude"])**2 + (df["Starting Station Longitude"] - df["Ending Station Longitude"])**2)**0.5
print(df["Distance"])

def degToRad(deg):
	return deg * (numpy.pi/180)

df["lat_dist"] = degToRad(df["Ending Station Latitude"] - df["Starting Station Latitude"])
df["long_dist"] = degToRad(df["Ending Station Longitude"] - df["Starting Station Longitude"])
df["temp_1"] = numpy.sin(df["lat_dist"]/2)**2 + numpy.cos(degToRad(df["Starting Station Latitude"])) * numpy.cos(degToRad(df["Ending Station Latitude"])) * numpy.sin(df["long_dist"]/2)**2
df["temp_2"] = 2 * numpy.arctan2(numpy.sqrt(df["temp_1"]), numpy.sqrt(1 - df["temp_1"]))
df["distance"] = 6371 * df["temp_2"]

final_distance = (str(round(df["distance"].mean(), 2)) + " km")

# regular commute?
df["Regular Commuter"] = df["Trip Route Category"].isin(['Round Trip']) & df["Passholder Type"].isin(['Monthly Pass'])
final_regular = (df["Regular Commuter"].value_counts()).tolist()

