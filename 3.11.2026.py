# from sqlalchemy import select, engine
#
# with engine.connect() as connection:
#     statement = select(students_table)
#     result = connection.execute(statement)
#
#     for row in result:
#         print(row.id, row.name, row.is_active)
#
#     statement2 = select(students_table.c.name, students_table.c.gpa)
#     result2 = connection.execute(statement2)
#     for row in result2:
#         print(row.name, row.gpa)




# from sqlalchemy import update, engine, delete
#
# with engine.connect() as connection:
#     statement = (
#         update(students_table)
#         .where(students_table.c.name == 'Петров П.П')
#         .values(gpa = 4.6)
#     )
#     result = connection.execute(statement)
#     connection.commit()
#     print(f"Обновлено строк: {result.rowcount}")
#
#     statement2 = delete(students_table).where(students_table.c.gpa < 3.5)
#     result = connection.execute(statement2)
#     connection.commit()


import json
from sqlalchemy import create_engine, insert, MetaData, Table, Column, Integer, String, Float, ForeignKey

engine = create_engine('sqlite:///shop.db', echo=True)
metadata = MetaData()
categories_table = Table(
    'categories', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100), unique=True, nullable=False),
    Column('description', String(255))
)
tovary_table = Table(
    'tovary', metadata,
    Column('id', Integer, primary_key=True),
    Column('product_name', String(200), nullable=False),
    Column('price', Float, nullable=False),
    Column('category_id', Integer, ForeignKey('categories.id'))
)

metadata.create_all(engine)
with open('catalog.json', 'r', encoding='utf-8') as file:
    catalog_data = json.load(file)

with engine.connect() as connection:
    categories_to_insert = []
    for item in catalog_data:
        cat_name = item['category']['name']
        cat_desc = item['category']['description']
        if (cat_name, cat_desc) not in categories_to_insert:
            categories_to_insert.append((cat_name, cat_desc))

    for cat in categories_to_insert:
        connection.execute(
            insert(categories_table).values(name=cat[0], description=cat[1])
        )
    connection.commit()

    result = connection.execute(categories_table.select())
    categories_dict = {}
    for row in result:
        categories_dict[row.name] = row.id


    for item in catalog_data:
        cat_name = item['category']['name']
        connection.execute(
            insert(tovary_table).values(
                product_name=item['product_name'],
                price=item['price'],
                category_id=categories_dict[cat_name]
            )
        )
    connection.commit()

