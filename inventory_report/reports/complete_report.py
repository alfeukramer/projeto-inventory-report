from inventory_report.reports.simple_report import SimpleReport


mocks = [{
    "id": 1,
    "nome_do_produto": "23423",
    "nome_da_empresa": "Forces",
    "data_de_fabricacao": "2022-05-05",
    "data_de_validade": "2023-02-4",
    "numero_de_serie": "FR48",
    "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
  }, {
    "id": 2,
    "nome_do_produto": "teste2",
    "nome_da_empresa": "Nature",
    "data_de_fabricacao": "1999-05-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48",
    "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
  }, {
    "id": 3,
    "nome_do_produto": "teste1",
    "nome_da_empresa": "Forces",
    "data_de_fabricacao": "2022-05-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48",
    "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
  }, {
    "id": 4,
    "nome_do_produto": "teste1",
    "nome_da_empresa": "Forces",
    "data_de_fabricacao": "2022-05-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48",
    "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
  }]

# manufacturing_date = min(item["data_de_fabricacao"] for item in data)
# most_products_company = max(item["nome_da_empresa"] for item in data)
# validation_data = []
# for item in data:
#     if item["data_de_validade"] > date.today().isoformat():
#         validation_data.append(item["data_de_validade"])


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data: list[dict]):
        simple_report = SimpleReport.generate(data)
        all_products = "Produtos estocados por empresa:\n"
        result = dict()

        for item in data:
            if item['nome_da_empresa'] in result:
                result[item['nome_da_empresa']] += 1
            else:
                result[item["nome_da_empresa"]] = 1

        for company, quantity in result.items():
            all_products += f"- {company}: {quantity}\n"

        return (
            f"{simple_report}\n"
            f"{all_products}"
            )
    # print(generate(mocks))
