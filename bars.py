import json
import sys


def load_data(bars_filepath):
    with open(bars_filepath) as bars_file:
        return json.load(bars_file)


def get_sit_counts(d_bars):
    return [d_bars["features"][bari]["properties"]["Attributes"]["SeatsCount"]
            for bari in range(len(d_bars["features"]))]


def get_biggest_bar(data_bars):
    sit_counts_list = get_sit_counts(data_bars)
    biggest_bar_index = sit_counts_list.index(max(sit_counts_list))
    return data_bars["features"][biggest_bar_index]


def get_smallest_bar(data_bars):
    sit_counts_list = get_sit_counts(data_bars)
    smallest_bar_index = sit_counts_list.index(min(sit_counts_list))
    return data_bars["features"][smallest_bar_index]


def get_closest_bar(data_bars, longitude, latitude):
    coordinates_list = [data_bars["features"][bari]["geometry"]["coordinates"]
                        for bari in range(len(data_bars["features"]))]
    distance_list = [abs(longitude - coordinates_list[bari][0]) +
                     abs(coordinates_list[bari][1] - latitude)
                     for bari in range(len(coordinates_list))]
    closest_index = distance_list.index(min(distance_list))
    return data_bars["features"][closest_index]


def get_bar_name(data_bar):
    return data_bar["properties"]["Attributes"]["Name"]


if __name__ == '__main__':
    try:
        data_bars = load_data(sys.argv[1])
        print("The biggest bar is " +
              get_bar_name(get_biggest_bar(data_bars)))
        print("The smallest bar is " +
              get_bar_name(get_smallest_bar(data_bars)))
        longitude, latitude = map(float,
                                  raw_input("Coordinates: ").split(' '))
        print("The closest bar is " +
              get_bar_name(get_closest_bar(data_bars, longitude, latitude)))
    except IndexError:
        print("No file name specified")
    except IOError as err2:
        print(err2)
    except ValueError as err3:
        print(err3)
