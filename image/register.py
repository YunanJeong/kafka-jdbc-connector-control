import os, json, string, requests

CONNECT_URL = os.getenv("CONNECT_URL")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
CONNECTION_URL_PREFIX = os.getenv("CONNECTION_URL_PREFIX", "jdbc:mysql://")

db_list = os.getenv("DB_LIST", "").split()
table_list = os.getenv("TABLE_LIST", "").split()
template = os.getenv("TEMPLATE_JSON")

for db_host in db_list:
    db_name = db_host
    for table in table_list:
        connector_name = f"{db_host}_{table}"
        print(f">>> Registering: {connector_name}")

        config_str = string.Template(template).substitute(
            DB=db_host,
            DB_HOST=db_host,
            DB_NAME=db_name,
            DB_USER=DB_USER,
            DB_PASS=DB_PASS,
            CONNECTION_URL_PREFIX=CONNECTION_URL_PREFIX,
            TABLE=table
        )

        config = json.loads(config_str)
        resp = requests.put(
            f"{CONNECT_URL}/connectors/{connector_name}/config",
            headers={"Content-Type": "application/json"},
            data=json.dumps(config)
        )
        print(f"{connector_name}: {resp.status_code}")
        print(resp.text)

print("✅ All connectors registered successfully.")
