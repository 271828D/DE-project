"""Script for the calculation of the
monthly metrics"""

import re
from dataclasses import dataclass
import pandas as pd


@dataclass(frozen=True)  # Keep the object inmutable
class MonthlyMetrics:
    """
    State the classes for single month
    metrics
    """

    month_year: str
    total_item_promo_discount: float
    total_item_price: float


def clean_date_string(date_str: str) -> str:
    """
    To extract valid date (%YYYY-%mm-%dd) patterns
    from corrupted strings (i.e. "2025-04-29ñá¿").

    The function use regular expressions to find
    date patterns.

    Args: date_str: Possible corrupted date string

    Returns:
        Cleaned date string or original if no
        pattern is found.
    """

    date_str = str(date_str)  # Convert date to string

    # Regular expression pattern for YYYY-MM-DD format
    # \d{4} = exactly 4 digits (year)
    # \d{2} = exactly 2 digits (month and day)
    pattern = r"\d{4}-\d{2}-\d{2}"

    match = re.search(pattern, date_str)  # Search for the pattern in the str

    if match:
        # Extract matched text
        return match.group(0)  # Returns "YYYY-MM-DD"
    else:
        return date_str  # Returns original


def clean_price_string(price_str: str) -> str:
    """
    Extract valid number pattern from corrupted strings."

    The function rescue the numeric values from the
    prices that has other characters attached.

    Args:
        price_str: Price string

    Returns:
        Price without corrupted characters or original
        (if no corrupted character found)
    """
    price_str = str(price_str)  # Ensures work with str values
    # Pattern: keep an eye on this as is matching values <= 0
    pattern = r"-?\d+\.?\d*"
    match = re.search(pattern, price_str)  # Search for the pattern
    # Logic
    if match:
        return match.group(0)
    else:
        return price_str


def data_preparation(df: pd.DataFrame) -> pd.DataFrame:
    """Prepare the dataframe for metric calculation"""

    df = df.copy()  # Keep copy of original df
    # Creating new col with object converted to str
    df["purchased_date_original"] = df["purchased_date"].astype(str)
    # Apply the clean_date_string function
    df["purchased_date_cleaned"] = df["purchased_date"].apply(
        clean_date_string
    )
    # Clean NA, NaN, empty instances after the clen date process
    df = df.dropna(subset=["purchased_date_cleaned"])
    # Filter "nan" strings
    df = df[df["purchased_date_cleaned"].astype(str).str.lower() != "nan"]

    # Convert object column to date objects col
    df["purchased_date"] = pd.to_datetime(
        df["purchased_date_cleaned"], errors="coerce"
    )

    df["month_year"] = df["purchased_date"].dt.to_period(
        "M"
    )  # Extract YYYY-MM
    df = df[~df["month_year"].isna()].copy()  # Removing NaT values
    df["month_year"] = df["month_year"].astype(
        str
    )  # To str without NaT values

    df["item_price_cleaned"] = df["item_price"].apply(
        clean_price_string
    )  # Cleaning step item_price, this keep values <= 0
    df["item_promo_discount_cleaned"] = df["item_promo_discount"].apply(
        clean_price_string  # Cleaning step item_promo_discount, this keep values <= 0
    )

    # Additionally after check and rescue corrupted values i need to erase NA rows
    df["item_price"] = pd.to_numeric(
        df["item_price_cleaned"], errors="coerce"
    )  # item_price to numeric
    # item_promo_discount to numeric
    df["item_promo_discount"] = pd.to_numeric(
        df["item_promo_discount_cleaned"], errors="coerce"
    )

    df = df.dropna(
        subset=["item_price", "item_promo_discount"], how="any"
    )  # Dropna values
    return df


def calculate_monthly_metrics(df_clean: pd.DataFrame) -> list[MonthlyMetrics]:
    """
    Calculate the monthly metrics from clean df.
    """
    df_prepared = data_preparation(df_clean)

    monthly_groups = (
        df_prepared.groupby("month_year")  # Group by col: month_year
        .agg(
            {"item_promo_discount": "sum", "item_price": "sum"}
        )  # agregates value for each group
        .reset_index()
    )

    monthly_groups["total_item_price"] = (
        monthly_groups["item_price"] - monthly_groups["item_promo_discount"]
    )
