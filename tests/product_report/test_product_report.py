from inventory_report.inventory.product import Product


def test_relatorio_produto():
    mock = Product(
        id=1,
        nome_do_produto="Cafe",
        nome_da_empresa="Cafes Nature",
        data_de_fabricacao="2020-07-04",
        data_de_validade="2023-02-09",
        numero_de_serie="FR48",
        instrucoes_de_armazenamento="instrucao",
    )

    mock_return = (
        "O produto Cafe fabricado em 2020-07-04 por Cafes Nature"
        " com validade até 2023-02-09 precisa ser armazenado instrucao."
    )

    assert str(mock) == mock_return
