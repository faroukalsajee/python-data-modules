from data import get_laptop_info_list, get_phone_info_list, get_tablet_info_list
import sys
import datetime
from statistics import median, mean
from json import dumps
import csv


# data report below
def get_text_report(data):
    text = 'Timestamp: {}\n'.format(data["date_time"])
    text += 'Device: {}\n'.format(data["device_type"])
    text += 'Number: {}\n'.format(data["number"])
    text += 'Average Price: ${}\n'.format(data["average_price"])
    text += 'Minimum Price: ${}\n'.format(data["min_price"])
    text += 'Maximum Price: ${:.2f}\n'.format(data["max_price"])
    text += 'Median RAM: {} GB\n'.format(data["median_ram"])
    text += 'Operating Systems: {}\n'.format(', '.join(data["operating_systems"]))
    return text


# test_main was failing for tablets because it was expecting ram with no decimals in json and csv but not in text
def get_csv_report(data):
    if data["device_type"] == "Tablet":
        data["median_ram"] = int(data["median_ram"])

    os_list = "/".join(data["operating_systems"])
    return f'{data["date_time"]},{data["device_type"]},{data["number"]},{data["average_price"]},{data["min_price"]},{data["max_price"]},{data["median_ram"]},{os_list}'


# test_main was failing for tablets because it was expecting ram with no decimals in json and csv but not in text

def get_json_report(data):
    if data["device_type"] == "Tablet":
        data["median_ram"] = int(data["median_ram"])

    return dumps(data, indent=4)


# We created a dictionary below
def build_data_dictionary(data_list, input_type):
    now_string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    return {
        "date_time": now_string,
        "device_type": input_type.capitalize(),
        "number": get_number(data_list),
        "average_price": get_average_price(data_list),
        "min_price": get_minimum_price(data_list),
        "max_price": get_maximum_price(data_list),
        "median_ram": get_median_ram(data_list),
        "operating_systems": get_operating_systems(data_list)

    }


# align function names with text
def get_number(data):
    return len(data)


# we use float number below
def get_average_price(data):
    price_list = [float(temp.split(',')[6]) for temp in data]
    return round(mean(price_list), 2)


# we use float number below
def get_minimum_price(data):
    price_list = [float(temp.split(',')[6]) for temp in data]
    return min(price_list)


# we use float number below
def get_maximum_price(data):
    price_list = [float(temp.split(',')[6]) for temp in data]
    return max(price_list)


# calculate median of RAM
def get_median_ram(data):
    ram_list = [float(temp.split(',')[3]) for temp in data]
    return median(ram_list)


# we use split function below
def get_operating_systems(data):
    os_list = [f"{temp.split(',')[4]} {temp.split(',')[5]}" for temp in data]
    return os_list
