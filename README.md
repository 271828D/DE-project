# Data Processing Pipeline

A Python script to download, clean, and generate reports from CSV data.

### **Prerequisites**
- Python 3.10+
- UV package manager ([installation guide](https://github.com/astral-sh/uv))

## **Quick Start**

### 1. Install UV (if not installed)
```
# Install development environment
curl -LsSf https://astral.sh/uv/install.sh | sh
```
### 2. Setup Env
```
# Create virtual environment and install dependencies
uv venv .venv --python 3.10
uv sync --dev
```
### 3. Activate virtual environment
```
source .venv/bin/activate
```
### 4. Run the Application
```
# Run with example URL
uv run --active python main.py --url "https://storage.googleapis.com/nozzle-csv-exports/testing-data/order_items_data_2_.csv"
```

**Note: Conda support is deprecated.**

## **What It Does**
1. **Downloads** the CSV file from the provided URL
2. **Cleans** the data:
        - Removes duplicate rows
        - Removes empty rows
3. **Generates** Reports:

        - ```processing_stats.json``` - Statistics about the cleaning process
        - ```monthly_metrics.csv``` - Monthly aggregated metrics (total prices and discounts per month)
        - ```discarded_rows.csv``` - Log of all removed rows

## **Output Files**
All reports are saved in the ```data/``` folder:
1. ```order_items_<timestamp>.csv```
2. ```discarded_rows.csv```
3. ```processing_stats.json```
```
{
    "total_rows": int,
    "total_empty_rows_removed": int,
    "total_invalid_rows_discarded": int,
    "total_duplicate_rows_removed": int,
    "total_usable_rows": int
}
```

4. ```monthly_metrics.csv```

| month_year | total_item_promo_discount | total_item_price |
|------------|---------------------------|------------------|
| 2025-01    | 12,444,303.37            | 70,550,200.07    |
| 2025-02    | 11,240,559.38            | 63,598,463.35    |
| 2025-03    | 12,484,082.41            | 70,795,796.21    |
| 2025-04    | 12,052,204.42            | 68,280,241.96    |
| 2025-05    | 12,476,208.51            | 70,717,750.66    |

## **Legacy Conda Support (Deprecated)**
If you still need to use conda:
```
conda env create -f environment.yml
conda activate coding_task
```
**Note: Conda support is deprecated. Please migrate to UV for better performance and modern Python packaging standards.**
