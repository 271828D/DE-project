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


def data_preparation(df: pd.DataFrame) -> pd.DataFrame:
    """Prepare the dataframe for metric calculation"""

    df = df.copy  # Keep copy of original df

    # Convert object column to date objects col
    df["purchased_date"] = pd.to_datetime(
        df["purchased_date"], errors="coerce"
    )
