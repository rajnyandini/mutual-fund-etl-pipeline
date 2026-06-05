import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:/// ABC_mf.db")

raw = "data/raw/ ABC_MF_Datasets/"
processed = "data/processed/"

# Load datasets
fund_master = pd.read_csv(raw + "01_fund_master.csv")
nav = pd.read_csv(processed + "02_nav_history_clean.csv")
aum = pd.read_csv(raw + "03_aum_by_fund_house.csv")
sip = pd.read_csv(raw + "04_monthly_sip_inflows.csv")
category = pd.read_csv(raw + "05_category_inflows.csv")
folios = pd.read_csv(raw + "06_industry_folio_count.csv")
performance = pd.read_csv(processed + "07_scheme_performance_clean.csv")
transactions = pd.read_csv(processed + "08_investor_transactions_clean.csv")
holdings = pd.read_csv(raw + "09_portfolio_holdings.csv")
benchmark = pd.read_csv(raw + "10_benchmark_indices.csv")

# Load into SQLite
fund_master.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)
aum.to_sql("fact_aum", engine, if_exists="replace", index=False)

print("Database loaded successfully!")