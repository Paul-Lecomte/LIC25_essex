# Data Analytics with Python and Data Storage Reflection

## Assignment Title: COVID-19 Statistics Analysis in Switzerland

## Completion Requirements

Download a publicly available dataset (e.g., global temperature trends, e-commerce sales, or COVID-19 statistics). Using Python (Pandas and Matplotlib libraries), perform the following:

    Load and clean the dataset.
    Conduct a basic analysis (e.g., mean, median, trends, correlations).
    Create visualisations to showcase key insights (e.g., bar graphs, line charts).

Write a 200-word reflection comparing two storage models (e.g., SQL vs. NoSQL or cloud-based vs. local storage) based on the dataset’s structure and use case.

## Repository Layout

```
.
├── data/                  # Dataset(s) used for analysis
├── notebooks/             # Jupyter notebooks for analysis (optional)
├── scripts/               # Python scripts for loading, cleaning, analysis, and visualization
├── reports/               # Final reflection and any figures
└── README.md              # this file
```

## Steps

1. **Data Acquisition**: Download a COVID-19 dataset for Switzerland (e.g., from official sources like BAG or Our World in Data).
2. **Data Cleaning**: Use Pandas to handle missing values, correct data types, and filter relevant columns (canton, city, dates, cases, etc.).
3. **Analysis**: Compute basic statistics (mean, median) and look for trends over time and correlations between variables.
4. **Visualization**: Create charts (bar graphs for cantonal comparisons, line charts for time trends, etc.) to highlight clusters and patterns.
5. **Reflection**: Write a 200-word comparison of two storage models (e.g., SQL vs. NoSQL or cloud-based vs. local storage) in the context of this dataset.

## Getting Started

1. Create a virtual environment and install required packages:

    ```bash
    python -m venv .venv
    source .venv/bin/activate   # On Windows: .venv\Scripts\activate
    pip install pandas matplotlib
    ```

2. Place the dataset in the `data/` directory.
3. Run the analysis script(s) in `scripts/` or use the notebooks in `notebooks/`.
4. Generate visualizations and save them to `reports/figures/` (if created) or as specified in the script.
5. Write the reflection in `reports/reflection.md`.

## Notes

- The analysis should focus on clustering by canton and cities to show geographical patterns.
- Ensure visualizations are clear and labeled appropriately.
- The reflection should critically evaluate storage models for enterprise scenarios based on the dataset’s structure (e.g., time-series, geographical dimensions) and use case (analytical queries for trends/patterns).

## To-Do List

- [x] Create directory structure: data/, scripts/, notebooks/, reports/
- [x] Download a Swiss COVID-19 dataset and place in data/ (Zurich canton data from openZH)
- [x] Write Python script to load and clean the dataset
- [x] Perform basic analysis (mean, median, trends, correlations)
- [x] Create visualizations (bar graphs for cantonal comparisons, line charts for time trends)
- [x] Write 200-word reflection comparing storage models (SQL vs. NoSQL or cloud-based vs. local)
- [x] Save reflection in reports/reflection.md
- [x] Ensure visualizations are saved and labeled appropriately

## Skills Developed

    Data cleaning and analytics with Python.
    Visualisation of data insights.
    Critical thinking on storage models and their suitability for enterprise.
    scenarios

## Author

Lecomte Paul
