import os
import argparse
import json
import sqlite3
from db_builder import build_db
from ui import user_interface

DB_NAME = 'beverages'
BRANDS_JSON = 'brands.json'


def load_brands_data(brands_path):
    with open(brands_path) as f:
        brands_data = json.load(f)
    return brands_data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-db', '--db_folder', help='path to folder for db creation')
    parser.add_argument('-br', '--brands_path', help='absolute path to brands json file')
    args = parser.parse_args()

    cwd = os.getcwd()
    script_folder = os.path.dirname(os.path.realpath(__file__))

    db_folder = args.db_folder if args.db_folder else cwd
    db_path = os.path.join(db_folder, DB_NAME)
    if os.path.exists(db_path):
        os.remove(db_path)

    brands_path = args.brands_path if args.brands_path else os.path.join(script_folder, BRANDS_JSON)
    brands_data = load_brands_data(brands_path)

    with sqlite3.connect(db_path) as conn:
        build_db(brands_data, conn)
        cursor = conn.cursor()
        user_interface(cursor)


if __name__ == '__main__':
    main()
