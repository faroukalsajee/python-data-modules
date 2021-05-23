import sys
import reports
import data
import datetime


# update input as suitable
def main():
    if len(sys.argv) < 3:
        print("Invalid command arguments : should execute it as follows:")
        print("main.py 'input_type' 'report_type'")
        exit()

    input_type = sys.argv[1]
    if not (input_type == 'phone' or input_type == 'tablet' or input_type == 'laptop'):
        print("Input type must be either phone, table or laptop")
        exit()

    report_type = sys.argv[2]
    if not (report_type == 'text' or report_type == 'csv' or report_type == 'json'):
        print("wrong report type ")
        exit()

    report = get_report(input_type, report_type)
    print(report)
    return report


# report function below
def get_report(input_type, report_type):
    data_list = get_data(input_type)
    data = reports.build_data_dictionary(data_list, input_type)
    if report_type == 'text':
        return reports.get_text_report(data)
    elif report_type == 'csv':

        return reports.get_csv_report(data)

    elif report_type == 'json':

        return reports.get_json_report(data)


# input type below
def get_data(input_type):
    if input_type == 'phone':
        return data.get_phone_info_list()
    elif input_type == 'tablet':

        return data.get_tablet_info_list()

    elif input_type == 'laptop':

        return data.get_laptop_info_list()


if __name__ == "__main__":
    main()
