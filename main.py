# import json
# import re

# hymns = []

# with open('hymns.json', 'r') as f:
#     hymns = json.load(f)


# def extract_numbers(s: str):
#     return [int(x) for x in re.findall('\d+', s)]

# def extract_name(s: str):
#     return s.split('(')[0].replace(',','').strip()

# for hymn in hymns:   
#     if 'author' in hymn:
#         print(hymn['author'].split(' ')[-1],extract_name(hymn['author'].split(' ')[-1]))
#     # if 'published_at' in hymn:
#     #     hymn['published_at'] = int(hymn['published_at'])
        
    
# with open('hymns.json', 'w') as f:
#     json.dump(hymns, f, indent=2)

import sqlite3

def create_database_from_sql(sql_file, db_name):
    """
    Create an SQLite database from an SQL file.

    Args:
        sql_file (str): Path to the .sql file containing SQL commands.
        db_name (str): Name of the SQLite database file to create.
    """
    try:
        # Connect to the SQLite database (creates it if it doesn't exist)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        
        print(f"Connected to SQLite database: {db_name}")

        # Read the SQL file
        with open(sql_file, 'r', encoding='utf-8') as file:
            sql_script = file.read()

        # Execute the SQL script
        cursor.executescript(sql_script)
        print(f"Executed SQL script from {sql_file}")

        # Commit changes and close the connection
        connection.commit()
        print(f"Database {db_name} created successfully.")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

    finally:
        if connection:
            connection.close()
            print("SQLite connection closed.")

# Example usage
if __name__ == "__main__":
    sql_file_path = "create-db.sql"  # Path to your SQL file
    database_name = "hymns.db"  # Name of your SQLite database
    create_database_from_sql(sql_file_path, database_name)
