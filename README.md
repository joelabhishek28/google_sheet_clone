# Google Sheets Clone (Python-based Spreadsheet)

## Overview
This project is a Python-based Google Sheets clone that allows users to create, edit, and perform calculations on spreadsheets. It supports basic mathematical operations and ensures data quality.

## Features
- Perform basic mathematical operations
- UI resembling Google Sheets
- Flask-based backend

## Installation

### Prerequisites
Ensure you have Python installed (Python 3.7 or later recommended).

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/google-sheets-clone.git
   cd google-sheets-clone
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```sh
   python main.py
   ```
2. Open a browser and go to `http://127.0.0.1:5000`

## Supported Formulas
- SUM() - syntax =SUM (A1:A3),
-  AVERAGE()- syntax =AVERAGE (A1:A3),
-  MIN()- syntax =MIN (A1:A3),
-  MAX()- syntax =MAX (A1:A3)
-  COUNT() - syntax =COUNT (A1:A3)
-  TRIM() - syntax =TRIM (A1)
-  UPPER - syntax - UPPER (string)
-  LOWER - syntax - LOWER (string)

## Technologies Used
- Python
- Flask
- Jinja2 (for rendering templates)

