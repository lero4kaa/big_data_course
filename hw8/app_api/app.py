from flask import Flask
from cassandra_client import CassandraClient
import json


app = Flask(__name__)
host = 'cass-node'
port = 9042
keyspace = 'transactions'


@app.get("/transactions/fraud&uid=<uid>")
def get_fraud_transactions(uid):
    return json.dumps(client.get_fraud_transactions(uid), indent=4, sort_keys=True, default=str)

@app.get("/transactions&uid=<uid>&start_date=<start_date>&end_date=<end_date>")
def get_transactions_by_date(uid, start_date, end_date):
    return json.dumps(client.get_transactions_by_date(uid, start_date, end_date), indent=4, sort_keys=True, default=str)

@app.get("/transactions/largest&uid=<uid>")
def get_largest_transactions(uid):
    return json.dumps(client.get_largest_transactions(uid), indent=4, sort_keys=True, default=str)



if __name__ == "__main__":
    client = CassandraClient(host, port, keyspace)
    client.connect()
    app.run(host='0.0.0.0', port=8080)

