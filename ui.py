from queries import *

DB_TABLES = ['producers', 'categories', 'brands']
QUERIES = {1: get_brands_of_producer,
           2: get_brands_of_category,
           3: get_brands_of_producer_and_category,
           4: count_brands_by_producer,
           5: count_brands_by_category,
           6: count_brands_by_producer_and_category,
           7: get_max_priced_brand,
           8: get_max_priced_brand_per_producer,
           9: get_max_priced_brand_per_category}

QUERIES_OPTIONS = [str(num) + ' - ' + query.__name__.replace('_', ' ') for num, query in QUERIES.items()]


# NOT MINE - Taken from:
# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch08s11.html
def pp(cursor):
    rowlens = 0
    d = cursor.description
    if not d:
        return "#### NO RESULTS ###"
    names = []
    lengths = []
    rules = []
    data = cursor.fetchall()
    for dd in d:  # iterate over description
        l = dd[1]
        if not l:
            l = 12  # or default arg ...
        l = max(l, len(dd[0]))  # Handle long names
        names.append(dd[0])
        lengths.append(l)
    for col in range(len(lengths)):
        if rowlens:
            rls = [len(row[col]) for row in data if row[col]]
            lengths[col] = max([lengths[col]] + rls)
        rules.append("-" * lengths[col])
    formatting = " ".join(["%%-%ss" % l for l in lengths])
    result = [formatting % tuple(names), formatting % tuple(rules)]
    for row in data:
        result.append(formatting % row)
    return "\n".join(result)


def show_results(cursor):
    print(pp(cursor))


def show_db(cursor):
    for table in DB_TABLES:
        print('\n' + table.capitalize() + ':')
        cursor.execute(f'SELECT * FROM {table}')
        show_results(cursor)


def results_to_options(results):
    results_as_lst = [r[0] for r in results]
    options = {i+1: r for i, r in enumerate(results_as_lst)}
    str_options = [str(i) + ' - ' + r for i, r in options.items()]
    return options, str_options


def param_choice_interface(param, options, str_options):
    while True:
        param = int(input('\n'.join([f'\nPlease choose {param}:'] +
                                    str_options + [''])))
        if param in options:
            return options[param]
        else:
            print('invalid option, please choose again')


def parameterized_query_interface(cursor, query):
    producers = get_all_producers(cursor)
    producers_opts, producers_str_opts = results_to_options(producers)
    categories = get_all_categories(cursor)
    categories_opts, categories_str_opts = results_to_options(categories)
    if query == 1:
        producer = param_choice_interface('producer', producers_opts, producers_str_opts)
        show_results(QUERIES[query](cursor, producer))
    elif query == 2:
        category = param_choice_interface('category', categories_opts, categories_str_opts)
        show_results(QUERIES[query](cursor, category))
    elif query == 3:
        producer = param_choice_interface('producer', producers_opts, producers_str_opts)
        category = param_choice_interface('category', categories_opts, categories_str_opts)
        show_results(QUERIES[query](cursor, producer, category))


def query_interface(cursor):
    while True:
        query = int(input('\n'.join(['\nWhat do you want to query?'] +
                                    QUERIES_OPTIONS +
                                    ['10 - stop querying\n'])))
        if query in QUERIES:
            if 1 <= query <= 3:
                parameterized_query_interface(cursor, query)
            else:
                show_results(QUERIES[query](cursor))
        elif query == 10:
            return
        else:
            print('invalid option, please choose again')


def user_interface(cursor):
    while True:
        option = int(input('\n'.join(['\nHello, what do you wish to do?',
                                      '1 - show DB',
                                      '2 - query something',
                                      '3 - quit\n'])))
        if option == 1:
            show_db(cursor)
        elif option == 2:
            query_interface(cursor)
        elif option == 3:
            return
        else:
            print('invalid option, please choose again')
