import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".xml" in path:
            with open(path, mode="r", encoding="utf-8") as file:
                xml_reader = xmltodict.parse(file.read())
                xml_reader = xml_reader['dataset']['record']
                return xml_reader
        else:
            raise ValueError("Arquivo inválido")
