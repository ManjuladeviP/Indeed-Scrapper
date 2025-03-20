# Indeed Scraper

## Overview
This Indeed Scraper is a Python-based tool designed to extract job postings from Indeed. It collects job titles, company names, locations, salaries (if available), and job descriptions, providing structured job data for analysis or job hunting.

## Features
- Scrapes job listings from Indeed based on keyword and location.
- Extracts job title, company name, location, salary, and job description.
- Saves data in CSV or JSON format for easy analysis.
- Uses BeautifulSoup and requests for web scraping.

## Requirements
Ensure you have the following dependencies installed before running the scraper:

```sh
pip install requests beautifulsoup4 pandas
```

## Usage
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/indeed-scraper.git
   cd indeed-scraper
   ```
2. Run the scraper:
   ```sh
   python scraper.py --keyword "Software Engineer" --location "New York"
   ```

### Command-line Arguments
| Argument       | Description                                      |
|---------------|--------------------------------------------------|
| `--keyword`   | Job title or keyword (e.g., "Data Scientist")    |
| `--location`  | Job location (e.g., "San Francisco, CA")        |
| `--pages`     | Number of pages to scrape (default is 1)        |
| `--output`    | Output file format (`csv` or `json`, default: csv) |

Example:
```sh
python scraper.py --keyword "Python Developer" --location "Remote" --pages 3 --output json
```

## Output
The scraped job listings are stored in `output.csv` or `output.json` in the same directory.

## Legal & Ethical Considerations
- This scraper should be used for personal and educational purposes only.
- Scraping Indeed may violate their Terms of Service. Use responsibly.
- Avoid overloading Indeed's servers; set appropriate request delays.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.
