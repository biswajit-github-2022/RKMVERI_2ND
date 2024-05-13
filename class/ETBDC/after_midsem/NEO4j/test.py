import re
from py2neo import Graph, Node, Relationship

def parse_relief_data(text):
    country_pattern = r"Country\s+([^\:]+)\:\:\:"
    city_item_pattern = r"([A-Za-z]+)\:([^\n]+)"

    countries = re.findall(country_pattern, text)
    data = {}
    for country in countries:
        print(country)
        data[country] = {}

        # Extract the text section for each country
        country_section_start = text.find(country)
        country_section_end = text.find("Country", country_section_start + 1)
        country_section = text[country_section_start:country_section_end]

        city_items = re.findall(city_item_pattern, country_section)
        for city, items in city_items:
            print(city)
            items_dict = {}
            items_list = re.split(r',|and', items)
            for item in items_list:
                item_parts = item.strip().rsplit(" ", 1)
                if len(item_parts) == 2:
                    item_name, quantity = item_parts
                    items_dict[item_name.strip()] = quantity.strip()
            data[country][city] = items_dict

    return data

def add_relief_data(graph, country_name, city_name, items):
    country = Node("Country", name=country_name)
    city = Node("City", name=city_name)
    graph.merge(country, "Country", "name")
    graph.merge(city, "City", "name")

    located_in = Relationship(city, "LOCATED_IN", country)
    graph.merge(located_in)

    for item_name, quantity in items.items():
        item = Node("Item", name=item_name, quantity=quantity)
        graph.merge(item, "Item", "name")

        distributed = Relationship(city, "DISTRIBUTED", item)
        graph.merge(distributed)

# Connect to the Neo4j database
graph = Graph("http://localhost:7474", auth=("neo4j", "neo4j123"))

# Example passage
text = """
Country Bangladesh:::
Bagerhat: 100 saris and 25 lungis on 18 November.
Chittagong: 1250 kg rice, 150 kg pulses, 350 saris, 50 dhotis, 104 gents’ garments and 46 ladies’ garments in October.
Dhaka: 679 saris from 18 to 20 October.
Faridpur: 350 saris from 20 to 24 October.

"""

# Parse the data
parsed_data = parse_relief_data(text)

# Add the data to the graph
for country, cities in parsed_data.items():
    for city, items in cities.items():
        add_relief_data(graph, country, city, items)
