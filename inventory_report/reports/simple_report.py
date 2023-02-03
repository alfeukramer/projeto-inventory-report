from datetime import date


class SimpleReport:
    @staticmethod
    def generate(data: list[dict]):
        today_date = date.today().isoformat()
        manufacturing_date = []
        companies = []
        validation_data = []

        for item in data:
            manufacturing_date.append(item["data_de_fabricacao"])

        for item in data:
            companies.append(item["nome_da_empresa"])

        for item in data:
            if item["data_de_validade"] > today_date:
                validation_data.append(item["data_de_validade"])

        return (
            f"Data de fabricação mais antiga: {min(manufacturing_date)}\n"
            f"Data de validade mais próxima: {min(validation_data)}\n"
            f'Empresa com mais produtos: {max(companies, key=companies.count)}'
            )
