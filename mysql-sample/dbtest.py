
from google.oauth2 import service_account
from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy
import json
import time


project_id = "rahul-research-test"
region = "asia-south1"
instance_name = "curefit-test-rahul"
INSTANCE_CONNECTION_NAME = "rahul-research-test:asia-south1:curefit-test-rahul"#f"{project_id}:{region}:{instance_name}" # i.e demo-project:us-central1:demo-instance
print(f"Your instance connection name is: {INSTANCE_CONNECTION_NAME}")
DB_USER = "rahulraj" 
DB_PASS = "rahulraj31" 
DB_NAME = "curefit_test_db" 

def main():
    with open('rahul-research-test-6dd22e92abfd.json') as source:
        info = json.load(source)

    cred = service_account.Credentials.from_service_account_info(info)

    # initialize Connector object
    connector = Connector(credentials=cred)

    # function to return the database connection object
    def getconn():
        conn = connector.connect(
            INSTANCE_CONNECTION_NAME,
            "pymysql",
            user=DB_USER,
            password=DB_PASS,
            db=DB_NAME,
            # ip_type=IPTypes.PRIVATE
        )
        return conn

    # create connection pool with 'creator' argument to our connection object function
    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,
    )

    with pool.connect() as db_conn:
        results = db_conn.execute(sqlalchemy.text("SELECT * FROM iris_data LIMIT 5")).fetchall()

      # show results
        for row in results:
            print(row)


if __name__ == "__main__":
    iter=1
    while True:
        print(f"Starting new Iteration No. {iter}")
        main()
        iter+=1
        time.sleep(5)

