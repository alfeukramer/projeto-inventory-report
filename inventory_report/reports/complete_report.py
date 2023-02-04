from inventory_report.reports.simple_report import SimpleReport


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
