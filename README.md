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
  The minimum requirements:
- Docker for Mac: [Docker >= 20.10.2](https://docs.docker.com/docker-for-mac/install/)
- Docker for Windows: 
  - Installation: [Docker](https://docs.docker.com/desktop/install/windows-install/)
  - Manual installation steps for older WSL version: [Docker WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)

### Instructions on how to execute the code
- Copy the `.env.example` file to `.env` and fill out the environment vars.

- Make sure you are executing the code from the etl_pipeline folder and you have Docker Desktop running.


To run it locally first build the image.

```bash
  docker image build -t etl .
```

Then run the etl job using docker:
```bash
  docker run --env-file .env etl
```