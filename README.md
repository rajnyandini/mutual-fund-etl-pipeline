# Mutual Fund ETL Pipeline

## Overview

This project implements an ETL (Extract, Transform, Load) pipeline for mutual fund data.

The pipeline extracts raw mutual fund information, cleans and transforms the data, and loads it into a structured database for further analysis and reporting.

## Project Components

### Data Ingestion

* Collects mutual fund data from configured sources.
* Stores raw records for processing.

### Data Cleaning

* Handles missing values.
* Removes duplicate records.
* Standardizes formats and data types.
* Performs basic validation checks.

### Database Loading

* Creates database tables using SQL schema definitions.
* Loads cleaned data into the database.

## Project Structure

```text
.
├── data_ingestion.py      # Extract data
├── clean_data.py          # Transform and clean data
├── create_database.py     # Create database and load data
├── schema.sql             # Database schema
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* Pandas
* SQL
* SQLite
* Git & GitHub

## ETL Workflow

1. Extract mutual fund data.
2. Clean and validate records.
3. Create database schema.
4. Load processed data into the database.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python data_ingestion.py
python clean_data.py
python create_database.py
```

## Security

Sensitive information such as API keys, credentials, and environment variables are excluded from version control through `.gitignore`.

## Future Improvements

* Automated scheduling
* Incremental data loading
* Data quality monitoring
* Dashboard integration
* Cloud deployment

## Author

Rajnandini Singh Solanki
