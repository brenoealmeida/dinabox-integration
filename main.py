"""Modulo para manipulação de arquivos .json"""
import json


def read_file(id_file):
    """Função para ler e retornar os dados do JSON"""
    with open(f"{id_file}.json", encoding='UTF-8') as file:
        data = json.load(file)
        woodwork_data1 = data["woodwork"]
        holes_data1 = data["holes"]
        components_data1 = data["components"]["data"]
    return woodwork_data1, holes_data1, components_data1


def calculate_sales_price(woodwork, holes, components):
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

    for key, value in components.items():
        for component in value["category_data"]:
            sale_price += component["parent"][0]["sale_price"]

    return sale_price


def calculate_category_costs(categories, woodwork, holes, components):
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
                category_costs[component["category_name"]] += (
                    component["factory_price"])
            else:
                not_found = component["category_name"]
                print(f"Categoria não encontrada: {not_found}")

    for hole in holes:
        category_costs["Rafix"] += hole["factory_price"]

    for key, value in components.items():
        for component in value["category_data"]:
            component_category = component["parent"][0]["category_name"]
            component_cost = component["parent"][0]["factory_price"]
            if component_category in category_costs.keys():
                category_costs[component_category] += component_cost
            else:
                print(f"Categoria não encontrada: {component_category}")

    return category_costs


def calculate_all_costs(category_costs):
    """Função para calcular o custo total do projeto"""
    total_costs = 0
    for cost in category_costs.values():
        total_costs += cost
    return total_costs


def calculate_new_sale_price(category_prices):
    """Função para calcular o novo valor de venda total do projeto"""
    total_price = 0
    for cost in category_prices.values():
        total_price += cost
    return total_price


def calculate_new_sale_price_by_category(categories, category_costs):
    """Função para calcular o preço de venda de acordo com os mark-ups"""
    category_sale_price = {
        category[0]: category_costs[category[0]] * category[1]
        for category in categories
    }

    return category_sale_price


# PROJECT_ID = input("Insira o ID do ambiente: ")
PROJECT_ID = "0881281641"

mkp_mdf = float(input("Insira o Mark-Up para MDF: "))
mkp_basic = float(input("Insira o Mark-Up para Ferragens Básicas: "))
mkp_special = float(input("Insira o Mark-up para Ferragens Especiais:"))
mkp_rafix = float(input("Insira o Mark-Up para Rafix: "))
mkp_outsourced = float(input("Insira o Mark-Up para Terceirizados: "))

woodwork_data, holes_data, components_data = read_file(PROJECT_ID)

sales_price = calculate_sales_price(woodwork_data, holes_data, components_data)
print(f"O valor de venda do Dinabox é R$ {sales_price:.2f}")

CATEGORIES = [("Acessórios", mkp_basic),
              ("Ferragens Básicas", mkp_basic),
              ("Ferragens Especiais", mkp_special),
              ("Ferragens BLUM e afins", mkp_outsourced),
              ("Perfis e Puxadores", mkp_basic),
              ("Porta de Alumínio", mkp_outsourced),
              ("Terceirizados", mkp_outsourced),
              ("Iluminação", mkp_outsourced),
              ("Vidraçaria", mkp_outsourced),
              ("Trilhos", mkp_basic),
              ("MDFs", mkp_mdf),
              ("Fitas", mkp_mdf),
              ("Fita 22mm", mkp_mdf),
              ("Fita 60mm", mkp_mdf),
              ("Rafix", mkp_rafix),
              ("Outros", 0),
              ]

category_cost = calculate_category_costs(CATEGORIES, woodwork_data, holes_data, components_data)

all_costs = calculate_all_costs(category_cost)
print(f"O custo total do projeto é R$ {all_costs:.2f}")

new_sale_price_by_category = calculate_new_sale_price_by_category(
    CATEGORIES, category_cost)
print("O valor de venda de cada categoria é:")
for category in new_sale_price_by_category:
    print(f"    {category}: R$ {new_sale_price_by_category[category]:.2f}")

new_price = calculate_new_sale_price(new_sale_price_by_category)
print(f"O valor final do projeto é R$ {new_price:.2f}")
