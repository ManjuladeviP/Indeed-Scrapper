# Crunchbase Lead Generator

## Overview
This script automates the process of scraping company data from Crunchbase, performing exploratory data analysis (EDA), and training a machine learning model to identify potential leads. It uses Selenium for web scraping, BeautifulSoup for parsing HTML, and Scikit-learn for modeling.

## Features
- Scrapes company data from Crunchbase
- Extracts details such as funding amount, industry, location, employee count, and founding year
- Uses sample data when scraping is not available
- Performs Exploratory Data Analysis (EDA) with Seaborn and Matplotlib
- Trains a machine learning model (Random Forest Classifier) to predict potential leads
- Identifies high-probability investment opportunities

## Requirements
Ensure you have the following installed before running the script:

- Python 3.x
- Google Chrome (latest version)
- ChromeDriver (managed via `webdriver-manager`)
- Required Python libraries:
  - `selenium`
  - `webdriver-manager`
  - `beautifulsoup4`
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`

## Installation
1. Clone this repository or download the script.
2. Install dependencies by running:
   ```sh
   pip install selenium webdriver-manager beautifulsoup4 pandas numpy matplotlib seaborn scikit-learn
   ```
3. Ensure Chrome is installed on your system.

## Usage
Run the script using:
```sh
python crunchbase_lead_generator.py
```
By default, the script scrapes 5 pages of Crunchbase data, trains a model, and identifies potential leads.

## Customization
- Modify the `scrape_crunchbase(num_pages=5)` function to change the number of pages scraped.
- Adjust the `get_potential_leads(threshold=0.7)` function to filter leads based on probability.
- Update the model parameters in `train_model()` to improve predictions.

## Legal Disclaimer
Scraping Crunchbase without permission may violate its [Terms of Service](https://www.crunchbase.com/terms). Ensure compliance by reviewing their policies or using authorized APIs.
