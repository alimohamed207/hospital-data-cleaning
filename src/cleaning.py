"""Reusable cleaning helpers for the hospital data cleaning portfolio project."""
from __future__ import annotations
import numpy as np
import pandas as pd

MISSING_MARKERS = {"n/a", "nan", "null", "unknown", "-", ""}

def normalize_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Trim text fields and normalize common text markers to pandas missing values."""
    result = df.copy()
    for col in result.select_dtypes(include=["object", "string"]).columns:
        result[col] = result[col].astype("string").str.strip()
        result.loc[result[col].str.casefold().isin(MISSING_MARKERS), col] = pd.NA
    return result

def clean_bill_amount(series: pd.Series) -> pd.Series:
    """Convert currency-like strings to numeric and mark negative amounts as missing."""
    cleaned = (series.astype("string").str.replace("$", "", regex=False)
               .str.replace(",", "", regex=False).str.strip())
    values = pd.to_numeric(cleaned, errors="coerce").astype("float64")
    return values.mask(values < 0, np.nan)

def clean_age(series: pd.Series, minimum: int = 0, maximum: int = 120) -> pd.Series:
    """Convert ages to numeric and mark values outside the configured range as missing."""
    values = pd.to_numeric(series, errors="coerce")
    return values.mask(~values.between(minimum, maximum), np.nan)
