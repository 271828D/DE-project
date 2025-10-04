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
### 3. Run the Application
```
# Run with example URL
uv run python main.py --url "https://storage.googleapis.com/nozzle-csv-exports/testing-data/order_items_data_2_.csv"
```

## Activate virtual environment
```
source .venv/bin/activate
```
### Available Commands
```
make           # Show all available commands
make install   # Setup development environment
make test      # Run tests
make format    # Format code with black
make lint      # Check code quality
make clean     # Remove virtual environment
make run       # Run the application
```

### Manual Setup (without Make)
If you don't have make installed:
```
# Create virtual environment
uv venv coding_task --python 3.10

# Activate it
source coding_task/bin/activate

# Install dependencies
uv sync --dev

# Install pre-commit hooks
pre-commit install
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

1. ```monthly_metrics.csv```
        **TO DO**

## **Legacy Conda Support (Deprecated)**
If you still need to use conda:
```
conda env create -f environment.yml
conda activate coding_task
```
**Note: Conda support is deprecated. Please migrate to UV for better performance and modern Python packaging standards.**
