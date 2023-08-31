## ETL Pipeline V.1
### Introduction

Building an ETL pipeline that runs the following steps:
- using sql query extracting the data from redshift with some transformations:
  - joining two tables online_transactions and stock_description
  - removing all rows where customer id is missing
  - removing corrupted stock codes
  - adding description to the online transactions table
  - replacing missing stock description with Unknown
  - fixing data type
- finding and dropping duplicates in the data
- loading the data to s3 bucket

### Requirements 
Python - 3.11 version was used

Libraries - listed in [requirements.txt](./requirements.txt)

### Instructions

1. Install the libraries you need from [requirements.txt](./requirements.txt) using ``` 
pip3 install -r requirements ```
2. Copy [.env.example](./.env.example) `.env` and fill the environment variables.
3. Run [main.py](./main.py) that performs the above-mentioned extraction, transformation and load tasks

