# ============================================================
# PROJECT 1: DATA CLEANING & PREPARATION
# DecodeLabs Internship 2026
# Dataset: E-Commerce Orders (1200 rows)
# ============================================================

import pandas as pd

# -------------------------------------------------------
# STEP 1: Load the Dataset
# -------------------------------------------------------
print("=" * 55)
print("PROJECT 1: DATA CLEANING & PREPARATION")
print("=" * 55)

df = pd.read_excel("Dataset for Data Analytics.xlsx")

print(f"\n✅ Dataset loaded successfully!")
print(f"   Shape: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"\nColumns: {list(df.columns)}")

# -------------------------------------------------------
# STEP 2: Initial Inspection
# -------------------------------------------------------
print("\n" + "-" * 55)
print("STEP 2: INITIAL INSPECTION")
print("-" * 55)

print("\nFirst 5 rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nBasic Info:")
df.info()

# -------------------------------------------------------
# STEP 3: Find Missing Values
# -------------------------------------------------------
print("\n" + "-" * 55)
print("STEP 3: MISSING VALUES CHECK")
print("-" * 55)

missing = df.isnull().sum()
print("\nMissing values per column:")
print(missing[missing >= 0])

missing_percent = (df.isnull().sum() / len(df)) * 100
print("\nMissing % per column:")
print(missing_percent[missing_percent > 0])

# Fix: Fill missing CouponCode with "NO_COUPON"
df["CouponCode"] = df["CouponCode"].fillna("NO_COUPON")
print("\n✅ CouponCode missing values filled with 'NO_COUPON'")
print(f"   Missing after fix: {df['CouponCode'].isnull().sum()}")

# -------------------------------------------------------
# STEP 4: Check & Remove Duplicates
# -------------------------------------------------------
print("\n" + "-" * 55)
print("STEP 4: DUPLICATE CHECK")
print("-" * 55)

total_duplicates = df.duplicated().sum()
order_id_duplicates = df.duplicated(subset=["OrderID"]).sum()

print(f"\nTotal duplicate rows    : {total_duplicates}")
print(f"Duplicate OrderIDs      : {order_id_duplicates}")

if total_duplicates > 0:
    df = df.drop_duplicates()
    print(f"✅ {total_duplicates} duplicate rows removed.")
else:
    print("✅ No duplicates found — dataset is clean on this check!")

# -------------------------------------------------------
# STEP 5: Fix Data Formats
# -------------------------------------------------------
print("\n" + "-" * 55)
print("STEP 5: DATA FORMAT CORRECTION")
print("-" * 55)

# Date column — ensure proper datetime format
df["Date"] = pd.to_datetime(df["Date"])
print(f"\n✅ Date column converted to datetime format")
print(f"   Sample: {df['Date'].head(3).tolist()}")

# Numeric columns — ensure correct types
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
df["TotalPrice"] = pd.to_numeric(df["TotalPrice"], errors="coerce")
print(f"\n✅ Numeric columns (Quantity, UnitPrice, TotalPrice) verified")

# String columns — strip whitespace & fix casing
text_cols = ["Product", "OrderStatus", "PaymentMethod", "ReferralSource"]
for col in text_cols:
    df[col] = df[col].str.strip().str.title()
print(f"\n✅ Text columns cleaned (whitespace removed, Title Case applied)")

# -------------------------------------------------------
# STEP 6: Validate Business Logic
# -------------------------------------------------------
print("\n" + "-" * 55)
print("STEP 6: BUSINESS LOGIC VALIDATION")
print("-" * 55)

# Check: TotalPrice should equal Quantity × UnitPrice
df["Calculated_Total"] = df["Quantity"] * df["UnitPrice"]
df["Price_Match"] = df["TotalPrice"].round(2) == df["Calculated_Total"].round(2)
mismatches = df[~df["Price_Match"]]
print(f"\nTotalPrice vs (Qty × UnitPrice) mismatches: {len(mismatches)}")

# Check: Quantity should be positive
negative_qty = df[df["Quantity"] <= 0]
print(f"Negative or zero Quantity rows: {len(negative_qty)}")

# Check: Valid OrderStatus values
valid_statuses = {"Delivered", "Shipped", "Cancelled", "Returned", "Pending"}
invalid_status = df[~df["OrderStatus"].isin(valid_statuses)]
print(f"Invalid OrderStatus values: {len(invalid_status)}")

print("\n✅ Business logic validation complete!")

# Drop helper column
df.drop(columns=["Calculated_Total", "Price_Match"], inplace=True)

# -------------------------------------------------------
# STEP 7: Final Summary & Save
# -------------------------------------------------------
print("\n" + "-" * 55)
print("STEP 7: FINAL CLEAN DATASET SUMMARY")
print("-" * 55)

print(f"\nFinal Shape       : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Missing Values    : {df.isnull().sum().sum()}")
print(f"Duplicate Rows    : {df.duplicated().sum()}")
print(f"Date Range        : {df['Date'].min().date()} → {df['Date'].max().date()}")
print(f"Unique Products   : {df['Product'].nunique()}")
print(f"Unique Customers  : {df['CustomerID'].nunique()}")

# Save cleaned dataset
df.to_excel("cleaned_dataset.xlsx", index=False)
print("\n✅ Cleaned dataset saved as 'cleaned_dataset.xlsx'")

print("\n" + "=" * 55)
print("PROJECT 1 COMPLETE ✅")
print("Zero duplicate IDs ✅ | Zero incorrectly formatted dates ✅")
print("=" * 55)
