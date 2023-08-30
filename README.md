## ETL Pipeline V.1
### Introduction

Building an ETL pipeline that runs the following steps:
- using sql query extracting the data from redshift with some transformations:
  - joining two tables online_transactions and stock_description
  - cleaning the data 
- finding and dropping duplicates in the data
- loading the data to s3 bucket

### Requirements 
Python - 3.11 version was used

Libraries - install from requirements.txt using:

```pip3 install -r requirements```

