import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Set up plotting style
plt.style.use('seaborn-v0_8')
plt.rcParams['figure.figsize'] = (12, 8)

def load_swiss_covid_data(filepath):
    """
    Load Swiss COVID-19 data from CSV file
    """
    print(f"Loading data from {filepath}")
    df = pd.read_csv(filepath)
    print(f"Data shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    return df

def clean_covid_data(df):
    """
    Clean the COVID-19 dataset
    """
    print("Cleaning data...")

    # Make a copy to avoid modifying original
    cleaned_df = df.copy()

    # Convert date column to datetime
    if 'date' in cleaned_df.columns:
        cleaned_df['date'] = pd.to_datetime(cleaned_df['date'])
        print("Converted 'date' column to datetime")

    # Handle missing values - fill numeric columns with 0 for cumulative counts
    numeric_cols = cleaned_df.select_dtypes(include=[np.number]).columns
    cleaned_df[numeric_cols] = cleaned_df[numeric_cols].fillna(0)
    print(f"Filled missing values in {len(numeric_cols)} numeric columns")

    # For text columns, fill with appropriate values
    text_cols = cleaned_df.select_dtypes(include=['object']).columns
    cleaned_df[text_cols] = cleaned_df[text_cols].fillna('')
    print(f"Filled missing values in {len(text_cols)} text columns")

    # Remove any completely empty rows
    cleaned_df = cleaned_df.dropna(how='all')

    print(f"Cleaned data shape: {cleaned_df.shape}")
    return cleaned_df

def basic_analysis(df):
    """
    Perform basic analysis on the COVID-19 data
    """
    print("\n=== BASIC ANALYSIS ===")

    # Check if we have the essential columns
    if 'ncumul_conf' in df.columns and 'date' in df.columns:
        # Get the latest data
        latest_date = df['date'].max()
        latest_data = df[df['date'] == latest_date]

        print(f"Latest data date: {latest_date}")
        print(f"Total cumulative confirmed cases: {latest_data['ncumul_conf'].sum():,.0f}")
        print(f"Total cumulative tested: {latest_data['ncumul_tested'].sum():,.0f}" if 'ncumul_tested' in latest_data.columns else "Tested data not available")

        if 'ncumul_deceased' in df.columns:
            print(f"Total cumulative deceased: {latest_data['ncumul_deceased'].sum():,.0f}")

        if 'ncumul_released' in df.columns:
            print(f"Total cumulative released: {latest_data['ncumul_released'].sum():,.0f}")

        # Calculate positivity rate if we have both tested and confirmed
        if 'ncumul_tested' in df.columns and 'ncumul_conf' in df.columns:
            total_tested = latest_data['ncumul_tested'].sum()
            total_confirmed = latest_data['ncumul_conf'].sum()
            if total_tested > 0:
                positivity_rate = (total_confirmed / total_tested) * 100
                print(f"Overall positivity rate: {positivity_rate:.2f}%")

    # Show data info
    print("\nData Info:")
    print(df.info())

    # Show descriptive statistics for numeric columns
    print("\nDescriptive Statistics:")
    print(df.describe())

    return df

def create_visualizations(df, output_dir='reports/figures'):
    """
    Create visualizations for the COVID-19 data
    """
    print(f"\nCreating visualizations in {output_dir}")

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Check if we have the necessary columns for time series analysis
    if 'date' in df.columns and 'ncumul_conf' in df.columns:
        # Aggregate by date (sum across cantons if we have multiple)
        daily_data = df.groupby('date')['ncumul_conf'].sum().reset_index()

        # 1. Line chart: Cumulative cases over time
        plt.figure(figsize=(14, 8))
        plt.plot(daily_data['date'], daily_data['ncumul_conf'], linewidth=2, color='darkred')
        plt.title('Swiss COVID-19 Cumulative Confirmed Cases Over Time', fontsize=16, fontweight='bold')
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Cumulative Confirmed Cases', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'swiss_covid_cumulative_cases.png'), dpi=300, bbox_inches='tight')
        plt.close()
        print("Saved: swiss_covid_cumulative_cases.png")

        # 2. Line chart: Daily new cases (calculate difference)
        daily_data['new_cases'] = daily_data['ncumul_conf'].diff().fillna(0)
        # Ensure no negative values (data reporting issues)
        daily_data['new_cases'] = daily_data['new_cases'].clip(lower=0)

        plt.figure(figsize=(14, 8))
        plt.plot(daily_data['date'], daily_data['new_cases'], linewidth=2, color='darkblue', alpha=0.7)
        plt.title('Swiss COVID-19 Daily New Cases Over Time', fontsize=16, fontweight='bold')
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Daily New Cases', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'swiss_covid_daily_new_cases.png'), dpi=300, bbox_inches='tight')
        plt.close()
        print("Saved: swiss_covid_daily_new_cases.png")

        # 3. Bar chart: Cases by canton (if we have canton data)
        if 'abbreviation_canton_and_fl' in df.columns:
            # Get latest data for each canton
            latest_date = df['date'].max()
            latest_canton_data = df[df['date'] == latest_date]

            # Aggregate by canton
            canton_cases = latest_canton_data.groupby('abbreviation_canton_and_fl')['ncumul_conf'].sum().sort_values(ascending=False)

            plt.figure(figsize=(14, 8))
            canton_cases.plot(kind='bar', color='darkgreen', alpha=0.8)
            plt.title(f'Swiss COVID-19 Cumulative Cases by Canton (as of {latest_date.strftime("%Y-%m-%d")})',
                     fontsize=16, fontweight='bold')
            plt.xlabel('Canton', fontsize=12)
            plt.ylabel('Cumulative Confirmed Cases', fontsize=12)
            plt.xticks(rotation=45)
            plt.grid(True, alpha=0.3, axis='y')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'swiss_covid_cases_by_canton.png'), dpi=300, bbox_inches='tight')
            plt.close()
            print("Saved: swiss_covid_cases_by_canton.png")

            # 4. Horizontal bar chart for better readability of canton names
            plt.figure(figsize=(12, 10))
            canton_cases.plot(kind='barh', color='darkgreen', alpha=0.8)
            plt.title(f'Swiss COVID-19 Cumulative Cases by Canton (as of {latest_date.strftime("%Y-%m-%d")})',
                     fontsize=16, fontweight='bold')
            plt.xlabel('Cumulative Confirmed Cases', fontsize=12)
            plt.ylabel('Canton', fontsize=12)
            plt.grid(True, alpha=0.3, axis='x')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'swiss_covid_cases_by_canton_horizontal.png'), dpi=300, bbox_inches='tight')
            plt.close()
            print("Saved: swiss_covid_cases_by_canton_horizontal.png")

def main():
    """
    Main function to run the analysis pipeline
    """
    print("Swiss COVID-19 Data Analysis")
    print("=" * 50)

    # File paths
    data_file = 'data/swiss_covid_zh.csv'  # Zurich canton data

    # Check if file exists
    if not os.path.exists(data_file):
        print(f"Error: Data file not found at {data_file}")
        print("Please download the data first.")
        return

    # Load data
    df_raw = load_swiss_covid_data(data_file)

    # Clean data
    df_clean = clean_covid_data(df_raw)

    # Basic analysis
    df_analyzed = basic_analysis(df_clean)

    # Create visualizations
    create_visualizations(df_analyzed)

    # Save cleaned data for future use
    output_path = 'data/swiss_covid_cleaned.csv'
    df_clean.to_csv(output_path, index=False)
    print(f"\nCleaned data saved to: {output_path}")

    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()