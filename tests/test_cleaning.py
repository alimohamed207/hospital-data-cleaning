import numpy as np
import pandas as pd

from src.cleaning import clean_age, clean_bill_amount, normalize_missing_values

def test_normalize_missing_values():
    frame = pd.DataFrame({"city": [" Cairo ", "unknown", None]})
    result = normalize_missing_values(frame)
    assert result.loc[0, "city"] == "Cairo"
    assert pd.isna(result.loc[1, "city"])
    assert pd.isna(result.loc[2, "city"])

def test_clean_bill_amount():
    result = clean_bill_amount(pd.Series(["$1,200.50", "25", "-4", "not available"]))
    assert result.iloc[0] == 1200.50
    assert result.iloc[1] == 25
    assert np.isnan(result.iloc[2])
    assert np.isnan(result.iloc[3])

def test_clean_age():
    result = clean_age(pd.Series(["34", "-1", "150", "unknown"]))
    assert result.iloc[0] == 34
    assert np.isnan(result.iloc[1])
    assert np.isnan(result.iloc[2])
    assert np.isnan(result.iloc[3])
