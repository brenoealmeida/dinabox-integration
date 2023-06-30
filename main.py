"""Modulo para manipulação de arquivos .json"""
import json


def read_file(id_file):
    """Função para ler e retornar os dados do JSON"""
    with open(f"{id_file}.json", encoding='UTF-8') as file:
        data = json.load(file)
        woodwork_data1 = data["woodwork"]
        holes_data1 = data["holes"]
    return woodwork_data1, holes_data1


def calculate_sales_price(woodwork, holes):
    """Função para calcular o valor de venda total do projeto"""

    sale_price = 0

    for modules in woodwork:
        parts = modules["parts"]
        inputs = modules["inputs"]
        for part in parts:
            sale_price += part["sale_price"]
        for component in inputs:
            sale_price += component["sale_price"]

    for hole in holes:
        sale_price += hole["sale_price"]

    return sale_price


def calculate_category_costs(categories, woodwork, holes):
    """Função para calcular os custos de cada categoria"""
    category_costs = {category[0]: 0 for category in categories}
    for modules in woodwork:
        parts = modules["parts"]
        inputs = modules["inputs"]
        for part in parts:
            category_costs["MDFs"] += part["material_factory"]
            category_costs["Fitas"] += part["edge_left_factory"]
            category_costs["Fitas"] += part["edge_right_factory"]
            category_costs["Fitas"] += part["edge_bottom_factory"]
            category_costs["Fitas"] += part["edge_top_factory"]
        for component in inputs:
            if component["category_name"] in category_costs.keys():
                category_costs[component["category_name"]] += component["factory_price"]
            else:
                not_found = component["category_name"]
                print(f"Categoria não encontrada: {not_found}")

    for hole in holes:
        category_costs["Rafix"] += hole["factory_price"]

    return category_costs


def calculate_all_costs(category_costs):
    """Função para calcular o custo total do projeto"""
    total_costs = 0
    for cost in category_costs.values():
        total_costs += cost
    return total_costs


PROJECT_ID = "0025124307"

woodwork_data, holes_data = read_file(PROJECT_ID)

sales_price = calculate_sales_price(woodwork_data, holes_data)
print(f"O valor de venda do Dinabox é R$ {sales_price:.2f}")

CATEGORIES = [("Acessórios", 2),
              ("Ferragens Básicas", 2),
              ("Ferragens Especiais", 2),
              ("Perfis e Puxadores", 2),
              ("Porta de Alumínio", 2),
              ("Terceirizados", 2),
              ("Iluminação", 2),
              ("Vidraçaria", 2),
              ("Trilhos", 2),
              ("MDFs", 2),
              ("Fitas", 2),
              ("Fita 22mm", 2),
              ("Rafix", 2),
              ("Outros", 2),
              ]

category_cost = calculate_category_costs(CATEGORIES, woodwork_data, holes_data)
print("Os custos de cada categoria são:")
for category in category_cost:
    print(f"    {category}: R$ {category_cost[category]:.2f}")

all_costs = calculate_all_costs(category_cost)
print(f"O custo total do projeto é R$ {all_costs:.2f}")
