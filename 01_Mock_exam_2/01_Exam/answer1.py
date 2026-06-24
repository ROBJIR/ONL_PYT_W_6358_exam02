# answer1.py
# - exam2
# robert.jiranek@gmail.com

import sys
from lib.lib_database import *


"""
database_connect={
        "host":"192.168.56.1",
        "port":"5432",
        "username":"cassiopeia",
        "userpwd":"central"
        }
"""

database_connect_postgres={
        "database": "postgres",
        "host":"192.168.56.1",
        "port":"5432",
        "username":"cassiopeia",
        "userpwd":"central"
        }

database_connect_exam2={
        "database": "exam2",
        "host":"192.168.56.1",
        "port":"5432",
        "username":"cassiopeia",
        "userpwd":"central"
        }

try:
    examdb=database()
    examdb.connect(connect_string=database_connect_postgres)
    examdb.sys_database_info(onscreen = True)
    # examdb.create_database("exam2222")
    # examdb.drop_database("exam22")
    examdb.close()

    examdb.connect(connect_string=database_connect_exam2)
    examdb.sys_database_info(onscreen = True)
    examdb.close()

except Exception as err:
    print(f"{68*"_"}\nERROR\n {err}\n{68*"_"}")
