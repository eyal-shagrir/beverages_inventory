def create_tables(cursor):
    cursor.executescript("""
                    CREATE TABLE brands (
                        pk              INTEGER          NOT NULL,
                        brand            TEXT             NOT NULL,
                        price           INTEGER          NOT NULL,
                        producer_fk     INTEGER          NOT NULL, 
                        category_fk     INTEGER          NOT NULL,

                        PRIMARY KEY(pk),
                        FOREIGN KEY(producer_fk)    REFERENCES producers(pk),
                        FOREIGN KEY(category_fk)    REFERENCES categories(pk)
                    );

                    CREATE TABLE producers (
                        pk              INTEGER     NOT NULL,
                        producer        TEXT        NOT NULL,

                        PRIMARY KEY(pk)
                    );

                    CREATE TABLE categories (
                        pk              INTEGER     NOT NULL,
                        category        TEXT        NOT NULL,

                        PRIMARY KEY (pk)
                    );
            """)


def fill_table(cursor, table, data, data_field):
    values_ids = {}
    for brand_data in data:
        field_value = brand_data[data_field]
        if field_value not in values_ids:
            cursor.execute(
                f'INSERT INTO {table}({data_field}) VALUES (?)',
                [field_value]
            )
            pk = cursor.lastrowid
            values_ids[field_value] = pk
    return values_ids


def build_db(brands_data, conn):
    cursor = conn.cursor()
    create_tables(cursor)
    producers = fill_table(cursor, 'producers', brands_data, 'producer')
    categories = fill_table(cursor, 'categories', brands_data, 'category')
    for brand_data in brands_data:
        brand = brand_data['brand']
        price = brand_data['price']
        producer_fk = producers[brand_data['producer']]
        category_fk = categories[brand_data['category']]
        cursor.execute(
            'INSERT INTO brands (brand, price, producer_fk, category_fk) '
            'VALUES (?, ?, ?, ?)',
            [brand, price, producer_fk, category_fk]
        )
