### Plagiarism-detection-using-string-matching-algorithms

Project Dependencies
1 2 3 4
Python 3.7 or higher
nltk
For tokenization, stemming, lemmatization, stopword removal, and other text preprocessing
tasks .
3
re
Pythonʼs built-in regular expressions module, for text cleaning and pattern matching.
Custom implementations for Rabin-Karp, Knuth-Morris-Pratt (KMP), and Longest Common
Subsequence (LCS)
py_stringmatching (optional)
Provides additional string similarity measures and tokenizers .
2
pandas
For structured data manipulation and exporting reports to CSV .
4
numpy
Required for efficient numerical operations, and as a dependency for many other libraries
.
2
4
Flask or Django
For building the web interface and backend API (choose one based on your project setup)
.
5
jinja2
(If using Flask) For HTML templating.
Flask-Login or Djangoʼs built-in authentication
For implementing login and registration pages (choose based on your web framework).
File Handling
Visualization/Highlighting
Testing
Optional/Advanced
python>=3.7
nltk
numpy>=1.7.0
pandas
Flask # or Django
jinja2
flask-login # if using Flask
python-docx
py-stringmatching
pytest
requests
Note:
python-docx
For handling .docx files if supporting more than plain text .
4
csv
Pythonʼs built-in module for reading and writing CSV files.
json
Pythonʼs built-in module for JSON report generation.
markupsafe or custom JavaScript/CSS
For highlighting matched text in the frontend.
pytest or unittest
For automated testing of modules and algorithms.
requests
For making HTTP requests if integrating with external APIs or cloud services .
4
BeautifulSoup and Selenium
Only if you plan to scrape web data or automate browser tasks .
4
Example requirements.txt
Install dependencies using pip install -r requirements.txt.
Adjust the list based on your actual implementation (e.g., if using Django, omit Flask and
related packages).
You may need additional packages for deployment or cloud integration if you expand the
project scope late
