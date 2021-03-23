from geopy.geocoders import Nominatim
import numpy as np
import argparse
import csv
import json


geolocator = Nominatim(user_agent="city-app")


def geolocate(city):
    """
    Finding longitudes and latitudes of cities in China
    :param city:
    :return:
    """
    country = "China"
    try:
        loc = geolocator.geocode(city + "," + country)
        return loc.latitude, loc.longitude
    except:
        return np.nan, np.nan


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("cities", type=str,
                        help="A csv file containing the cities to geolocate and their counts")
    parser.add_argument("output_file", type=str,
                        help="A json file to write the output to" )
    args = parser.parse_args()
    with open(args.output_file, "w") as file_out:
        for line in csv.DictReader(open(args.cities, "r")):
            line["latitude"], line["longitude"] = geolocate(line["city"])
            file_out.write(json.dumps(line) + "\n")

if __name__ == "__main__":
    main()