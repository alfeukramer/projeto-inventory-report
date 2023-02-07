from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory():
    @staticmethod
    def verify(data, type):
        if type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)

    @staticmethod
    def import_data(path, type_report):

        if ".csv" in path:
            data_csv_path = CsvImporter.import_data(path)
            # print("log do data_csv_path: ", data_csv_path)

            data_verify = Inventory.verify(data_csv_path, type_report)
            return data_verify

        elif ".json" in path:
            data_json_path = JsonImporter.import_data(path)
            data_verify = Inventory.verify(data_json_path, type_report)
            return data_verify

        elif ".xml" in path:
            data_xml_path = XmlImporter.import_data(path)
            data_verify = Inventory.verify(data_xml_path, type_report)
            return data_verify

        else:
            raise ValueError("Arquivo inválido")


print(Inventory.import_data("inventory_report/data/inventory.csv", "simples"))
