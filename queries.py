def get_all_producers(cursor):
    return cursor.execute('SELECT producer FROM producers '
                          'ORDER BY producer')


def get_all_categories(cursor):
    return cursor.execute('SELECT category FROM categories '
                          'ORDER BY category')


def get_brands_of_producer(cursor, producer):
    return cursor.execute('SELECT brand FROM brands '
                          'JOIN producers ON producer_fk = producers.pk '
                          'WHERE producer = ?',
                          [producer])


def get_brands_of_category(cursor, category):
    return cursor.execute('SELECT brand FROM brands '
                          'JOIN categories ON category_fk = categories.pk '
                          'WHERE category = ?',
                          [category])


def get_brands_of_producer_and_category(cursor, producer, category):
    return cursor.execute('SELECT brand FROM brands '
                          'JOIN producers ON producer_fk = producers.pk '
                          'JOIN categories ON category_fk = categories.pk '
                          'WHERE producer = ? AND category = ?',
                          [producer, category])


def count_brands_by_producer(cursor):
    return cursor.execute('SELECT producer, COUNT(brands.pk) FROM brands '
                          'JOIN producers ON producer_fk = producers.pk '
                          'GROUP BY producer_fk '
                          'ORDER BY COUNT(brands.pk) ASC')


def count_brands_by_category(cursor):
    return cursor.execute('SELECT category, COUNT(brands.pk) FROM brands '
                          'JOIN categories ON category_fk = categories.pk '
                          'GROUP BY category_fk '
                          'ORDER BY COUNT(brands.pk) ASC')


def count_brands_by_producer_and_category(cursor):
    return cursor.execute('SELECT producer, category, COUNT(brands.pk) FROM brands '
                          'JOIN producers ON producer_fk = producers.pk '
                          'JOIN categories ON category_fk = categories.pk '
                          'GROUP BY producer_fk, category_fk '
                          'ORDER BY producer ASC, COUNT(brands.pk) ASC')


def get_max_priced_brand(cursor):
    return cursor.execute('SELECT brand, max(price) FROM brands')


def get_max_priced_brand_per_producer(cursor):
    return cursor.execute('SELECT producer, brand, max(price) FROM brands '
                          'JOIN producers ON producer_fk = producers.pk '
                          'GROUP BY producer_fk '
                          'ORDER BY producer ASC')


def get_max_priced_brand_per_category(cursor):
    return cursor.execute('SELECT category, brand, max(price) FROM brands '
                          'JOIN categories ON category_fk = categories.pk '
                          'GROUP BY category_fk '
                          'ORDER BY category ASC')

