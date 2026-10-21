# Hospital Data Cleaning & Quality Analysis

A portfolio project demonstrating a structured data cleaning workflow with Python and Pandas. It inspects data quality, normalizes missing-value markers, standardizes categories, validates numeric fields and dates, creates a small set of derived features, and exports a cleaned dataset plus a quality report.

## Tools
Python · Pandas · NumPy · Jupyter · Matplotlib · Seaborn · Pytest

## Repository structure
```text
hospital-data-cleaning/
├── data/
│   ├── raw/                 # Place source CSV here; do not commit private data
│   └── processed/           # Generated outputs; ignored by Git
├── notebooks/
│   └── hospital_data_cleaning.ipynb
├── src/
│   └── cleaning.py          # Reusable helper functions
├── tests/
│   └── test_cleaning.py
├── reports/figures/
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting started
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Put your dataset at `data/raw/synthetic_hospital_dataset.csv`.
4. Open `notebooks/hospital_data_cleaning.ipynb` and run cells from top to bottom.

The notebook reads the included CSV from `data/raw/` by default.

## What the workflow covers
- Initial inspection and missingness profiling
- Normalization of common missing-value markers
- Exact duplicate removal and reporting of potential logical duplicates
- Text and categorical standardization
- Numeric conversion and range validation
- Email format checks and date consistency checks
- Length-of-stay and bill-per-day features
- Exploratory charts and a data quality report
- Export to `data/processed/hospital_cleaned.csv`

## Important assumptions
- Age range (0–120) and room-number range (100–799) are configurable example rules; validate them against actual business requirements.
- Similar patient attributes are not proof of a duplicate person. Potential logical duplicates are flagged for review rather than automatically deleted.
- Missing values are reported instead of universally filled with a median. Imputation should be selected per column and use case.
- Email validation checks format only; it does not verify that an address exists.

## Privacy
Only use synthetic or properly anonymized data. Do not publish identifiable patient information or confidential medical records. Raw and processed data files are excluded from Git by default.

## Tests
Run:
```bash
pytest
```

## Results
The dataset is synthetic and reproducible. Run the notebook from top to bottom to calculate the current metrics and export the cleaned dataset plus quality report. Do not treat the synthetic data as clinical evidence.

## Author
Ali Mohamed  
Aspiring Data Engineer | Python | Pandas | SQL | Data Quality
