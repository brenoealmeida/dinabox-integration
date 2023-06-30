import json

with open("data.json") as file:
    data = json.load(file)
    # x = data["woodwork"][0]["parts"][0]["sale_price"]

x = data["woodwork"]
y = data["holes"]

sale_price = 0

for pieces in x:
    parts = pieces["parts"]
    inputs = pieces["inputs"]
    for part in parts:
        sale_price += part["sale_price"]
    for input in inputs:
        sale_price += input["sale_price"]

for holes in y:
    sale_price += holes["sale_price"]

costs = 0

for pieces in x:
    parts = pieces["parts"]
    inputs = pieces["inputs"]
    for part in parts:
        costs += part["material_factory"]
        costs += part["edge_left_factory"]
        costs += part["edge_right_factory"]
        costs += part["edge_bottom_factory"]
        costs += part["edge_top_factory"]
    for input in inputs:
        costs += input["factory_price"]

for holes in y:
    costs += holes["factory_price"]


print(sale_price)
print(costs)
