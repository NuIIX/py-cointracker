import csv
import json
import os
import xml.etree.ElementTree as ET

def export_to_csv(data, file_path):
    """
    Экспортирует список объектов криптовалют (data) в CSV файл.
    """
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Symbol", "Price", "Market Cap", "Circulating Supply"])
        for crypto in data:
            writer.writerow([crypto.name, crypto.symbol, crypto.price, crypto.market_cap, crypto.circulating_supply])

def export_to_json(data, file_path):
    """
    Экспортирует список объектов криптовалют (data) в JSON файл.
    """
    export_list = []
    for crypto in data:
        export_list.append({
            "Name": crypto.name,
            "Symbol": crypto.symbol,
            "Price": crypto.price,
            "Market Cap": crypto.market_cap,
            "Circulating Supply": crypto.circulating_supply
        })
    with open(file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(export_list, jsonfile, ensure_ascii=False, indent=4)

def export_to_xml(data, file_path):
    """
    Экспортирует список объектов криптовалют (data) в XML файл.
    """
    root = ET.Element("Cryptocurrencies")
    for crypto in data:
        crypto_elem = ET.SubElement(root, "Cryptocurrency")
        ET.SubElement(crypto_elem, "Name").text = crypto.name
        ET.SubElement(crypto_elem, "Symbol").text = crypto.symbol
        ET.SubElement(crypto_elem, "Price").text = str(crypto.price)
        ET.SubElement(crypto_elem, "MarketCap").text = str(crypto.market_cap)
        ET.SubElement(crypto_elem, "CirculatingSupply").text = str(crypto.circulating_supply)
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

def get_file_size(file_path):
    """
    Возвращает размер файла в удобном формате (Bytes, KB, MB, GB).
    """
    size = os.path.getsize(file_path)
    if size < 1024:
        return f"{size} Bytes"
    elif size < 1024 ** 2:
        return f"{size / 1024:.2f} KB"
    elif size < 1024 ** 3:
        return f"{size / (1024 ** 2):.2f} MB"
    else:
        return f"{size / (1024 ** 3):.2f} GB"
