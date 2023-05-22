# ics5114_jack_bugeja
 Big Data Processing Assignment - Jack Bugeja
 
**This project uses python3.10 & docker meaning both are needed on your system in order to run this project properly.
**

# Running The MySQL Server & Data Ingestion Script
1. clone this repository on your local machine
2. run ```pip install -r requirements.txt``` to install all of the required python librarues for the scripts in this project
3. run the docker-compose up -d in your terminal (within the project directory) to run the docker container containing the image and volume with the working mysql database and respective database data. The .tar file in the repository contains some sample data from the dataset due to size, as well as some database configs that should get the server up and running

![Screenshot 2023-05-21 at 10 54 43](https://github.com/Grampun/ics5114_jack_bugeja/assets/29627317/1cbe02d7-ac07-4851-b07e-efc71e30b20a)

4. change your current directory to ```cd /bdp_assignment/pub_sub_broker/src``` and run the command ```python3.10 pub_sub_link.py``` to execute the script responsible for fetching the data from the mysql server, and pushing it to GCP Pub/Sub (Message broker).

![image](https://github.com/Grampun/ics5114_jack_bugeja/assets/29627317/4a2dbaeb-18b9-4339-9721-56a69ac8110e)

5. Navigate to the Pub/Sub page within the GCP project, you should start to see some changes in the stats

![Screenshot 2023-05-21 at 11 01 57](https://github.com/Grampun/ics5114_jack_bugeja/assets/29627317/9fecc0f4-6bd8-41c6-9a84-9c12ba3c3a8e)

6. You may also navigate to the Dataflow job page, where you will see the job responsible for streaming the data from the Pub/Sub broker to the BigQuery data warehouse, where data will be pushed in the respective table. The Dataflow job page shows how many messages are being streamed into the BigQuery table per second. N.B Dataflow runs on Apache Beam.

![Screenshot 2023-05-21 at 11 09 11](https://github.com/Grampun/ics5114_jack_bugeja/assets/29627317/c662d615-4b7f-485c-b9ad-4dba2b6a46a2)

7. The BigQuery page shows a list of all the datasets and their respective tables, where you can query and transform the data.

![Screenshot 2023-05-21 at 11 11 49](https://github.com/Grampun/ics5114_jack_bugeja/assets/29627317/5b5bfe5e-99e0-4a02-8a41-276061b9556c)

8. The data from the BigQuery tables and BigQuery ML models can be found in this report: https://lookerstudio.google.com/reporting/6399820a-433d-47ab-a3e1-309044982035



# Architectural Diagram


![big_data_processing_jb drawio](https://github.com/Grampun/ics5114_jack_bugeja/assets/29627317/4cdf654f-0beb-48cf-b484-6f54a81297d9)


# Logging into your Viewing Account

1. You will find the credentials for the GCP viewing account in the readMe I uploaded through the VLE 
2. Use the credentials provided to log into GCP: https://console.cloud.google.com/
3. All of the GCP modules necessary for this assignment have been pinned to this account's sidebar:

![Screenshot 2023-05-21 at 11 29 12](https://github.com/Grampun/ics5114_jack_bugeja/assets/29627317/bb143509-b0d7-463c-a8ef-222627d69ae0)
