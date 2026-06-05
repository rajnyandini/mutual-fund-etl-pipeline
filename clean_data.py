import pandas as pd

# Paths
raw_path = "data/raw/ ABC/"
processed_path = "data/processed/"

# NAV HISTORY
nav = pd.read_csv(raw_path + "02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])

nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(processed_path + "02_nav_history_clean.csv", index=False)

print("NAV cleaned")

# INVESTOR TRANSACTIONS
txn = pd.read_csv(raw_path + "08_investor_transactions.csv")

txn["transaction_date"] = pd.to_datetime(txn["transaction_date"])

txn["transaction_type"] = txn["transaction_type"].str.strip()

txn = txn[
    txn["transaction_type"].isin(
        ["SIP", "Lumpsum", "Redemption"]
    )
]

txn = txn[txn["amount_inr"] > 0]

valid_kyc = ["Verified", "Pending"]

txn = txn[txn["kyc_status"].isin(valid_kyc)]

txn.to_csv(
    processed_path + "08_investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned")

# SCHEME PERFORMANCE
perf = pd.read_csv(raw_path + "07_scheme_performance.csv")

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf["expense_flag"] = (
    (perf["expense_ratio_pct"] < 0.1)
    |
    (perf["expense_ratio_pct"] > 2.5)
)

perf.to_csv(
    processed_path + "07_scheme_performance_clean.csv",
    index=False
)

print("Performance cleaned")

# CLEAN AND SAVE REMAINING DATASETS

files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    df = pd.read_csv(raw_path + file)

    df = df.drop_duplicates()

    clean_name = file.replace(".csv", "_clean.csv")

    df.to_csv(
        processed_path + clean_name,
        index=False
    )

    print(f"{clean_name} saved")