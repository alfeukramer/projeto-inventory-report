from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv


class Importer():
    @staticmethod
    def import_data(path, type_report):
        with open(path, mode="r", encoding="utf-8") as file:
            csv_reader = list(csv.DictReader(file, delimiter=","))

        if type_report == "completo":
            return CompleteReport.generate(csv_reader)

        elif type_report == "simples":
            return SimpleReport.generate(csv_reader)

    print(import_data("inventory_report/data/inventory.csv", "simples"))
