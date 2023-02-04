from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json
import xmltodict


class Inventory():
    @staticmethod
    def import_data(path, type_report):
        with open(path, mode="r", encoding="utf-8") as file:

            if ".csv" in path and type_report == "completo":
                csv_reader = list(csv.DictReader(file, delimiter=","))
                return CompleteReport.generate(csv_reader)

            elif ".csv" in path and type_report == "simples":
                csv_reader = list(csv.DictReader(file, delimiter=","))
                return SimpleReport.generate(csv_reader)

            elif ".json" in path and type_report == "completo":
                json_reader = json.load(file)
                return CompleteReport.generate(json_reader)

            elif ".json" in path and type_report == "simples":
                json_reader = json.load(file)
                return SimpleReport.generate(json_reader)

            elif ".xml" in path and type_report == "simples":
                    xml_reader = xmltodict.parse(file.read())['dataset']['record']
                    return SimpleReport.generate(xml_reader)

            elif ".xml" in path and type_report == "completo":
                    xml_reader = xmltodict.parse(file.read())['dataset']['record']
                    return CompleteReport.generate(xml_reader)

    print(import_data("inventory_report/data/inventory.xml", "simples"))
