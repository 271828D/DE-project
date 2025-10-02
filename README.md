# Data Processing Pipeline

A Python script to download, clean, and generate reports from CSV data.

## Environment Setup

This project uses **conda** for environment management.

### **Option 1: Using Conda (Recommended)**

1. Create the environment from `environment.yml`:
   ```bash
   conda env create -f environment.yml
   ```

2. Activate the environment:
   ```bash
   conda activate coding_task
   ```
### **Option 2: Using pip**
If you prefer pip, install from ```requirements.txt```:
```bash
pip install -r requirements.txt
```
## **Usage**
Run the script with a CSV file URL:
```bash
python main.py --url "CSV_URL_HERE"
```
### **Example**
```bash
python main.py --url "https://storage.googleapis.com/nozzle-csv-exports/testing-data/order_items_2_.csv"
```
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
```{
    "total_rows": int,
    "total_empty_rows_removed": int,
    "total_invalid_rows_discarded": int,
    "total_duplicate_rows_removed": int,
    "total_usable_rows": int
}```
4. ```monthly_metrics.csv```
        *TO DO*
