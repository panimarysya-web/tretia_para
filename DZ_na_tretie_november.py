import sqlite3
import json

def create_table_categories():
    conn = sqlite3.connect("shops.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS categories(id INTEGER PRIMARY KEY, name TEXT UNIQUE, description TEXT)")
    conn.commit()
    conn.close()

def create_table_tovary():
    conn = sqlite3.connect("shops.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tovary(id INTEGER PRIMARY KEY, product_name TEXT, price REAL, category_id INTEGER, FOREIGN KEY(category_id) REFERENCES categories(id))")
    conn.commit()
    conn.close()

def insert_categories(data):
    conn = sqlite3.connect("shops.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT OR IGNORE INTO categories (name, description) VALUES(?, ?)", data)
    conn.commit()
    conn.close()

def insert_tovary(data):
    conn = sqlite3.connect("shops.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO tovary (product_name, price, category_id) VALUES(?, ?, ?)", data)
    conn.commit()
    conn.close()

def get_category_id(name):
    conn = sqlite3.connect("shops.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM categories WHERE name = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

create_table_categories()
create_table_tovary()

with open('catalog.json', 'r', encoding='utf-8') as file:
    catalog_data = json.load(file)

categories_to_insert = []
products_to_insert = []

for item in catalog_data:
    cat_name = item['category']['name']
    cat_desc = item['category']['description']

    if (cat_name, cat_desc) not in categories_to_insert:
        categories_to_insert.append((cat_name, cat_desc))

insert_categories(categories_to_insert)

for item in catalog_data:
    prod_name = item['product_name']
    prod_price = item['price']
    cat_name = item['category']['name']
    cat_id = get_category_id(cat_name)
    products_to_insert.append((prod_name, prod_price, cat_id))

insert_tovary(products_to_insert)
