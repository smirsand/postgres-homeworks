"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os

import psycopg2

with psycopg2.connect(host='localhost', database='north', user='postgres', password='2721896') as conn:
    with conn.cursor() as cur:
        folder_path_1 = os.path.join('north_data', 'customers_data.csv')
        folder_path_2 = os.path.join('north_data', 'employees_data.csv')
        folder_path_3 = os.path.join('north_data', 'orders_data.csv')

        with open(folder_path_1, 'r', encoding='utf-8') as file, open(folder_path_2, 'r',
                                                                      encoding='utf-8') as file_1, open(
            folder_path_3, 'r', encoding='utf-8') as file_2:
            reader_1 = csv.DictReader(file)
            reader_2 = csv.DictReader(file_1)
            reader_3 = csv.DictReader(file_2)

            insert_query_1 = "INSERT INTO customers VALUES (%s, %s, %s)"
            insert_query_2 = "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)"
            insert_query_3 = "INSERT INTO orders VALUES (%s, %s, %s, %s, %s)"

            for row in reader_1:
                cur.execute(insert_query_1, (row['customer_id'], row['company_name'], row['contact_name']))

            for row in reader_2:
                cur.execute(insert_query_2, (
                    row['employee_id'], row['first_name'], row['last_name'], row['title'], row['birth_date'],
                    row['notes']))

            for row in reader_3:
                cur.execute(insert_query_3, (
                    row['order_id'], row['customer_id'], row['employee_id'], row['order_date'], row['ship_city']))

conn.close()
