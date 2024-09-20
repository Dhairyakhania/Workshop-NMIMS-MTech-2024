import sqlalchemy
import sqlite3
import pandas as pd

# TODO: Using Flask create API, which 
# 1. reads excel file 
# 2. writes data in sqlite database


@app.route("", methods = ['GET', 'POST'])
def read_excel_file_using_pandas():
    pd.read_excel("file_name")

@app.route("")
def create_sqlite_database():
    sqlite3.create_sqlite_database()


def insert_rows_in_database():
    for row in excel_file:
        database.insert(row)