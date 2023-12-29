import os
import cx_Oracle
from dotenv import load_dotenv



class orcldb:

    load_dotenv()
    api_username = os.getenv("API_USERNAME")
    api_pwd = os.getenv("API_PASSWORD")
    cx_Oracle.init_oracle_client(lib_dir=os.getenv('lib_dir'))
    pool = cx_Oracle.SessionPool(os.getenv("BLD_USERNAME"), os.getenv("BLD_PASSWORD"), f'{ os.getenv("BLD_HOST")}:{ os.getenv("BLD_PORT")}/{ os.getenv("BLD_SERVICE_NAME")}',
                             min = 2, max = 5, increment = 1, threaded = True,
                             getmode = cx_Oracle.SPOOL_ATTRVAL_WAIT)
    print(f"Successfully connected to Oracle Database {pool}")