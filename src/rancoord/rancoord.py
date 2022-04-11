# Importing Modules
from dis import dis
from typing import List, Tuple
from math import radians, cos, sin, asin, sqrt, atan, tan, atan2
from shapely.geometry import Polygon, Point
from geopy.geocoders import Nominatim
import folium
import datetime
import os
import random
import json
import csv
import xlsxwriter
import utils.constants as constants
import requests
import numpy as np

# Default polygon around the district of Lisbon, Portugal
# Use nominatim_geocoder() provided module or define the
# desired polygon (use: http://apps.headwallphotonics.com/)
poly = Polygon(
    [
        (38.78562804689748, -9.47276949903965),
        (38.713870245772654, -9.139059782242775),
        (38.89740476139506, -9.055975675797463),
        (38.96871087768789, -8.969115019059181),
        (39.05061092686942, -8.92894625685215),
        (39.08579612091302, -9.407538175797463),
        (38.984457987516386, -9.397238493180275),
    ]
)


def create_dir(dir_name: str = "data") -> None:
    """Auxiliar function to create a new directory. User can choose to name
    the specific location.

    Args:
        dir_name (optional): Directory name. Defaults to 'maps'.
    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def nominatim_geocoder(address: str) -> List:
    """
    Function to geocode an address using the Nominatim geocoder and return
    the bounding box of the address.

    Args:
        address (str): Address to geocode.

    Returns:
        List: List of coordinates of the bounding box.
    """
    geolocator = Nominatim(user_agent="hugodscarvalho/rancoord")
    location = geolocator.geocode(
        address,
        exactly_one=True,
        language="english",
        namedetails=True,
        addressdetails=True,
    )
    if isinstance(location, type(None)):
        raise ValueError(
            "The introduced adress was not found. \
        Please introduce a valid address."
        )
    else:
        bounding_box = location.raw["boundingbox"]

    return bounding_box


def polygon_from_boundingbox(boundingbox: List) -> Polygon:
    """
    Function to create a polygon from a bounding box.

    Args:
        boundingbox (List): List of coordinates of the bounding box.

    Returns:
        Polygon: Polygon created from the bounding box.
    """

    min_lat = float(boundingbox[0])
    max_lat = float(boundingbox[1])
    min_lon = float(boundingbox[2])
    max_lon = float(boundingbox[3])

    polygon = Polygon(
        [(min_lat, max_lon),
         (max_lat, max_lon),
         (max_lat, min_lon),
         (min_lat, min_lon)]
    )

    return polygon


def coordinates_randomizer(
    polygon: Polygon = poly,
    num_locations: int = 10,
    plot: bool = False,
    save: bool = False,
    matrix: bool = False,
) -> Tuple:
    """
    Given a polygon and a number of locations, the function will
    return a list of latitudes and longitudes that are randomly
    generated within the polygon.

    Args:
      polygon (Polygon): the polygon that you want to randomize points within
      num_locations (int): The number of sites to generate.
      plot (bool): If True, the coordinates will be plotted on a folium map.
      save (bool): If True, the map will be saved. Defaults to True.

    Returns:
      two lists, one with the latitudes and one with the longitudes.
    """

    # Defining the randomization generator
    min_x, min_y, max_x, max_y = polygon.bounds
    points = []
    while len(points) < num_locations:
        random_point = Point(
            [random.uniform(min_x, max_x), random.uniform(min_y, max_y)]
        )
        if random_point.within(polygon):
            points.append(random_point)
    lat = [point.x for point in points]
    lon = [point.y for point in points]

    dt = np.zeros(shape=(len(lat), len(lat)))

    if plot:
        plot_coordinates(lat, lon)
    if save:
        multiple_formats_saver(lat, lon)
    if matrix:
        dt = distance_matrix(lat, lon)

    return lat, lon, dt


def list_average(list_of_numbers: List) -> float:
    """
    Function to calculate the average of a list of numbers.

    Args:
        list_of_numbers (List): List of numbers.

    Returns:
        float: Average of the list of numbers.
    """

    return sum(list_of_numbers) / len(list_of_numbers)


def plot_coordinates(lat: List, lon: List, zoom: int = 11, save: bool = True):
    """
    Function to plot the coordinates on a folium map.

    Args:
        lat (List): List of latitudes.
        lon (List): List of longitudes.
        zoom (int): Zoom level of the map. Defaults to 11.
        save (bool): If True, the map will be saved. Defaults to True.

    Returns:
        map: Folium map with the coordinates.
    """
    avg_lat = list_average(lat)
    avg_lon = list_average(lon)
    date = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
    map = folium.Map(
        location=[avg_lat, avg_lon], zoom_start=zoom, tiles="CartoDB positron"
    )
    for lat, lon in zip(lat, lon):
        folium.Marker([lat, lon]).add_to(map)
    if save:
        create_dir("maps")
        map.save(f"maps/map_{date}.html")
    else:
        map

    return map


def multiple_formats_saver(
    lat: List,
    lon: List,
    columns: List = ["Latitude", "Longitude"],
    file_format: str = "json",
    file_name: str = "coordinates",
    dir_name: str = "coordinates",
) -> None:
    """
    This function saves the coordinates lat and lon as the names introduced
    in a given columns list ('Latitude' and 'Longitude' by default). The
    coordinates are saved in a given format introduced by the user among the
    possibilities csv, json, txt and xlsx (json by default) and the output
    file name is also given by the user as file_name. User can choose the
    directory name where the output file will be saved.

    Args:
        lat (List): List of latitude values
        lon (List): List of longitude values
        columns (List, optional): Column names. Defaults to ['Latitude',
            'Longitude'].
        file_format (str, optional): File format. Defaults to 'json'.
        file_name (str, optional): File name. Defaults to 'coordinates'.
        dir_name (str, optional): Directory name. Defaults to 'coordinates'.
    """
    assert len(lat) > 0, "No values found on the latitude list"
    assert len(lon) > 0, "No values found on the longitude list"
    assert len(lat) == len(lon), "The lists must have the same length"
    assert len(columns) > 0, "No column names found"
    assert len(columns) == 2, "The column names list must have two elements"
    assert file_format in [
        "csv",
        "json",
        "txt",
        "xlsx",
    ], "The file format must be one of the following: csv, json, txt or xlsx"
    assert file_name is not None, "No file name found"
    assert dir_name is not None, "No directory name found"

    create_dir(dir_name)
    date = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")

    _file_name = dir_name + "/" + file_name + "_" + date + "." + file_format
    lat_name = columns[0]
    lon_name = columns[1]

    _list = []

    for i in range(len(lat)):
        obj = {lat_name: lat[i], lon_name: lon[i]}
        _list.append(obj)

    if file_format == "csv":
        with open(_file_name, "w") as f:
            writer = csv.writer(f)
            writer.writerow([lat_name, lon_name])
            writer.writerows(zip(lat, lon))
    elif file_format == "json":
        with open(_file_name, "w") as f:
            json.dump(_list, f)
    elif file_format == "txt":
        with open(_file_name, "w") as f:
            f.write(f"{lat_name}\t{lon_name}\n")
            for x, y in zip(lat, lon):
                f.write(str(x) + "\t" + str(y) + "\n")
    elif file_format == "xlsx":
        workbook = xlsxwriter.Workbook(_file_name)
        worksheet = workbook.add_worksheet()
        head = [lat_name, lon_name]
        worksheet.write_row(0, 0, head)
        worksheet.write_column(1, 0, lat)
        worksheet.write_column(1, 1, lon)
        workbook.close()


def haversine_distance(
    pickup_lat: float,
    pickup_long: float,
    dropoff_lat: float,
    dropoff_long: float,
    miles=False,
):
    """
    The haversine formula is used to calculate the great-circle distance
    between two points on a sphere given their longitudes and latitudes.

    Args:
      pickup_lat: The latitude of the pickup location
      pickup_long: The longitude of the pickup location.
      dropoff_lat: The latitude of the dropoff location.
      dropoff_long: The longitude of the dropoff location.
      miles: Boolean. If True, the output will be in miles.
    If False, the output will be in kilometers. Defaults to False

    Returns:
      The distance between two points on a sphere.
    """
    # Coonvert decimal degrees to radians
    pickup_lat, pickup_long, dropoff_lat, dropoff_long = map(
        radians, [pickup_lat, pickup_long, dropoff_lat, dropoff_long]
    )

    # Haversine formula
    dlon = dropoff_long - pickup_long
    dlat = dropoff_lat - pickup_lat
    a = sin(dlat / 2) ** 2 + cos(pickup_lat) \
        * cos(dropoff_lat) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))

    # Radius of earth
    km = constants.a * c
    if miles:
        km *= constants.MILES_PER_KILOMETER  # kilometers to miles
    return round(km, 3)


def vincenty_distance(
    pickup_lat: float,
    pickup_long: float,
    dropoff_lat: float,
    dropoff_long: float,
    miles=False,
):
    """
    The function takes the latitude and longitude of two points on
    the Earth's surface and returns the distance between them in
    kilometers using the Vincenty formula.

    Args:
      pickup_lat: Latitude of the pickup location
      pickup_long: longitude of the pickup location
      dropoff_lat: Latitude of the dropoff location
      dropoff_long: Longitude of the dropoff location
      miles: If True, returns distance in miles,
    otherwise kilometers. Defaults to False

    Returns:
      The distance between two points on the earth using the vincenty formula.
    """

    # check for coincident locations
    if pickup_lat == dropoff_lat and pickup_long == dropoff_long:
        return 0.0

    U1 = atan((1 - constants.f) * tan(radians(pickup_lat)))
    U2 = atan((1 - constants.f) * tan(radians(dropoff_lat)))
    L = radians(dropoff_long - pickup_long)
    Lambda = L

    sinU1 = sin(U1)
    cosU1 = cos(U1)
    sinU2 = sin(U2)
    cosU2 = cos(U2)

    for iteration in range(constants.MAX_ITERATIONS):
        sinLambda = sin(Lambda)
        cosLambda = cos(Lambda)
        sinSigma = sqrt(
            (cosU2 * sinLambda) ** 2 + (cosU1 * sinU2 - sinU1 * cosU2 * cosLambda) ** 2
        )
        if sinSigma == 0:
            return 0.0  # coincident points
        cosSigma = sinU1 * sinU2 + cosU1 * cosU2 * cosLambda
        sigma = atan2(sinSigma, cosSigma)
        sinAlpha = cosU1 * cosU2 * sinLambda / sinSigma
        cosSqAlpha = 1 - sinAlpha**2
        try:
            cos2SigmaM = cosSigma - 2 * sinU1 * sinU2 / cosSqAlpha
        except ZeroDivisionError:
            cos2SigmaM = 0
        C = constants.f / 16 * cosSqAlpha * (4 + constants.f * (4 - 3 * cosSqAlpha))
        LambdaPrev = Lambda
        Lambda = L + (1 - C) * constants.f * sinAlpha * (
            sigma
            + C * sinSigma * (cos2SigmaM + C * cosSigma * (-1 + 2 * cos2SigmaM**2))
        )
        if abs(Lambda - LambdaPrev) < constants.CONVERGENCE_THRESHOLD:
            break  # successful convergence
    else:
        return None  # failure to converge

    uSq = cosSqAlpha * (constants.a**2 - constants.b**2) / (constants.b**2)
    A = 1 + uSq / 16384 * (4096 + uSq * (-768 + uSq * (320 - 175 * uSq)))
    B = uSq / 1024 * (256 + uSq * (-128 + uSq * (74 - 47 * uSq)))
    deltaSigma = (
        B
        * sinSigma
        * (
            cos2SigmaM
            + B
            / 4
            * (
                cosSigma * (-1 + 2 * cos2SigmaM**2)
                - B
                / 6
                * cos2SigmaM
                * (-3 + 4 * sinSigma**2)
                * (-3 + 4 * cos2SigmaM**2)
            )
        )
    )
    s = constants.b * A * (sigma - deltaSigma)

    if miles:
        s *= constants.MILES_PER_KILOMETER  # kilometers to miles
    return round(s, 3)


def osrm_distance(
    pickup_lat: float,
    pickup_long: float,
    dropoff_lat: float,
    dropoff_long: float,
    miles=False,
):
    """
    It takes in the pickup and dropoff coordinates and returns
    the distance between them in kilometers usin the OSRM API.

    Args:
      pickup_lat: the latitude of the pickup location
      pickup_long: the longitude of the pickup location
      dropoff_lat: The latitude of the dropoff location.
      dropoff_long: The longitude of the dropoff location.
      miles: If True, return the distance in miles. Otherwise,
      return the distance in kilometers. Defaults to False
    """

    loc = "{},{};{},{}".format(pickup_long, pickup_lat, dropoff_long, dropoff_lat)
    url = "http://router.project-osrm.org/route/v1/driving/"
    r = requests.get(url + loc)
    if r.status_code != 200:
        return {}

    res = r.json()
    distance = res["routes"][0]["distance"]
    km = distance * constants.KILOMETERS_PER_METER

    if miles:
        km *= constants.MILES_PER_KILOMETER  # kilometers to miles

    return round(km, 3)


def distance_matrix(lat: List, lon: List, method: str = 'vincenty'):
    """
    For each pair of geographic coordinates, calculate the distance between
    them using the specified method and return a matrix of distances.

    Args:
      lat (List): List of latitudes
      lon (List): List of longitudes
      method (str): The method to use to calculate the distance matrix.

    Returns:
      A matrix of distances between each pair of points.
    """

    if method == "haversine":
        return np.array(
            [
                [
                    haversine_distance(lat[i], lon[i], lat[j], lon[j])
                    for j in range(len(lat))
                ]
                for i in range(len(lat))
            ]
        )
    elif method == "vincenty":
        return np.array(
            [
                [
                    vincenty_distance(lat[i], lon[i], lat[j], lon[j])
                    for j in range(len(lat))
                ]
                for i in range(len(lat))
            ]
        )
    elif method == "osrm":
        return np.array(
            [
                [
                    osrm_distance(lat[i], lon[i], lat[j], lon[j])
                    for j in range(len(lat))
                ]
                for i in range(len(lat))
            ]
        )
    else:
        raise ValueError("Invalid method")