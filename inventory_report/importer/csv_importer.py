import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".csv" in path:
            with open(path, mode="r", encoding="utf-8") as file:
                csv_reader = list(csv.DictReader(file, delimiter=","))
                return csv_reader
        else:
            raise ValueError("Arquivo inválido")
