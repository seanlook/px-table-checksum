
db_host_src = '10.0.200.195'
db_host_dst = '10.0.200.195'

TABLES_CHECK = {"d_name": ["t_1", "t_2"],
                 "d_name2": ["t_3"]}

DB_SOURCE = {'db_host': db_host_src,
           'db_port': 3306,
           'db_user': 'ecuser',
           'db_pass': 'ecuser',
           'db_charset': 'latin1',
           'result_charset': 'latin-1'}

DB_TARGET = {'db_host': db_host_dst,
           'db_port': 3307,
           'db_user': 'ecuser',
           'db_pass': 'ecuser',
           'db_charset': 'utf8mb4',
           'result_charset': 'utf-8'}


DB_ID_CS = 'qa-crm0'
