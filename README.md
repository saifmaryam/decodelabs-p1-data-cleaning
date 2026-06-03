# 🧹 Project 1 — Data Cleaning & Preparation

> **Intern:** Data Analytics Track  
> **Organization:** [DecodeLabs.tech](https://www.decodelabs.tech)  
> **Batch:** 17-May-2026 to 17-June-2026 
> **Dataset:** E-Commerce Orders — 1,200 rows

---

## 🎯 Goal

Take raw, messy e-commerce order data and transform it into a clean, analysis-ready dataset. This is the foundation for all other projects.

---

## 🔍 What This Project Does

### Step 1 — Load Dataset
- Loaded 1,200 rows × 14 columns of raw e-commerce order data

### Step 2 — Initial Inspection
- Checked shape, data types, and first few rows
- Identified all column names and their types

### Step 3 — Missing Values
- Found **309 missing values** in `CouponCode` column
- Filled all missing values with `"NO_COUPON"`

### Step 4 — Duplicate Check
- Verified **zero duplicate OrderIDs**
- Dataset is clean on this check ✅

### Step 5 — Data Format Correction
- Converted `Date` column to proper `datetime` format
- Verified `Quantity`, `UnitPrice`, `TotalPrice` as numeric
- Applied `Title Case` and stripped whitespace from text columns

### Step 6 — Business Logic Validation
- Validated: `TotalPrice = Quantity × UnitPrice`
- Checked for negative quantities
- Verified all `OrderStatus` values are valid

### Step 7 — Save Cleaned Dataset
- Exported final clean data as `cleaned_dataset.xlsx`

---

## 📊 Results Summary

| Check | Result |
|-------|--------|
| Total Rows | 1,200 |
| Missing Values (before) | 309 |
| Missing Values (after) | 0 ✅ |
| Duplicate Rows | 0 ✅ |
| Date Format Fixed | ✅ |
| Text Columns Cleaned | ✅ |
| Business Logic Valid | ✅ |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-green?logo=pandas)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-Excel-lightgreen)

---

## 🏢 About DecodeLabs

**DecodeLabs.tech** — Industrial Training Program for aspiring developers and data analysts.  
📍 Greater Lucknow, India  
🌐 [www.decodelabs.tech](https://www.decodelabs.tech)

---

*Part of DecodeLabs Industrial Training — Batch 2026*
