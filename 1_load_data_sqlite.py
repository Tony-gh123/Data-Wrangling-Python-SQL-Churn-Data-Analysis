import sqlite3
import pandas as pd
import os

def main():
    # create database folder w/ db.sqlite file. | Add path below.
    db_path = r'__PATH__'
   
    #os.makedirs(os.path.dirname(db_path), exist_ok=True)
    # Connect to the database
    conn = sqlite3.connect(db_path)

    # add path to csv folder / Find CSV files
    csv_folder = r'__PATH__'

    csv_files = [f for f in os.listdir(csv_folder) if f.endswith('.csv')]

    # auto populate csv file in the sqlite database
    for csv_file in csv_files:
        table_name = os.path.splitext(csv_file)[0]
        file_path = os.path.join(csv_folder, csv_file)
        df = pd.read_csv(file_path)
        df.to_sql(table_name, conn, if_exists='replace', index=False)

    # print tables sucessfully created    
    tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
    print(tables)

    conn.close()

if __name__ == "__main__":
    main()

