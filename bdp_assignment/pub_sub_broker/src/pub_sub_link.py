from mysql.connector import connect
from google.cloud import pubsub_v1
import time
import os
import json
import pandas as pd
from tqdm import tqdm

credentials_path = "../service_account/ics5114-jack-bugeja-385315-54431bfbd120.json"

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path


#provide the topic path
topic_path = 'projects/ics5114-jack-bugeja-385315/topics/sea_levels_topic'

# MySQL database configuration
mysql_config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'era5_dataset'
}

# Connect to MySQL database
mysql_conn = connect(**mysql_config)
mysql_cursor = mysql_conn.cursor(buffered=True)

# Execute a MySQL query to fetch data and set longer timeouts
mysql_cursor.execute("SET SESSION net_read_timeout=28800")
mysql_cursor.execute("SET GLOBAL connect_timeout=28800")
mysql_cursor.execute("SET SESSION wait_timeout=28800")
mysql_cursor.execute('SELECT * FROM era5_table')
row_count = mysql_cursor.rowcount

# Define batch size and calculate number of batches
batch_size = 1000
num_batches = (row_count // batch_size) + 1

with tqdm(total=row_count, desc='Loading data from SQL') as pbar:
    # Fetch data in batches and store in a pandas dataframe
    data = []
    for i in range(num_batches):
        batch = mysql_cursor.fetchmany(batch_size)
        if not batch:
            break
        data += batch
        pbar.update(len(batch))

    df = pd.DataFrame(data, columns=[i[0] for i in mysql_cursor.description])
    df = df.dropna()
    print(df.size)

# result = df.reset_index().to_json(orient='index')
# json_obj = json.loads(result)

# Close the MySQL connection
print('Closing MySql connection...')
mysql_cursor.close()
mysql_conn.close()

# Create a pub/sub publisher/producer instance
print('Establishing connection with GCP Pub/Sub...')

batch_settings = pubsub_v1.types.BatchSettings(
    max_messages=10,  # default 100
    max_bytes=1024,  # default 1 MB
    max_latency=0.001,  # default 10 ms
)

publisher = pubsub_v1.PublisherClient(batch_settings)

# Setting up loop that pushes each dataset record to Pub/Sub Topic
for index, row in df.iterrows():
    # Convert the Python dictionary to a JSON string
    message = json.dumps(row.to_dict()).encode('utf-8')
    # Publish the JSON string to Pub/Sub
    future = publisher.publish(topic_path, data=message)
    #print('just finished pushing message: ' + future.result() + ' to Pub/Sub')
