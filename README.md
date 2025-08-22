# How to Generate `credentials.json`

Follow these steps to create and download your `credentials.json` file for Google Sheets and Drive API access:

🔹 **Step 1: Enable Google Sheets & Drive API**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (e.g., `GoogleSheetsAPI`)
3. In the project, go to **API Library**
	- Enable **Google Sheets API**
	- Enable **Google Drive API**

🔹 **Step 2: Create Service Account & JSON Key**
1. In Cloud Console, go to **APIs & Services → Credentials**
2. Click **Create Credentials → Service Account**
3. Enter a name for the service account, then click **Create**
4. Assign the **Editor** role, then click **Done**
5. Open the Service Account you just created
6. Go to **Keys → Add Key → JSON**
7. Download the `credentials.json` file and save it in your project folder

---
# Google Sheets with Python

This project demonstrates how to interact with Google Sheets using Python. You will learn how to read, write, and update data in Google Sheets programmatically.

## Features
- Connect to Google Sheets using Python
- Read and write data
- Update existing sheets
- Authentication using Google API credentials

## Prerequisites
- Python 3.x
- `pandas` library
- Google API credentials (`credentials.json`)

## Setup
1. **Clone the repository**
2. **Install dependencies**:
	```powershell
	pip install pandas
	pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
	```
3. **Obtain Google API credentials**:
	- Go to [Google Cloud Console](https://console.cloud.google.com/)
	- Create a new project and enable the Google Sheets API
	- Create credentials and download the `credentials.json` file
	- Place `credentials.json` in the project root

## Usage
1. Run the main script:
	```powershell
	python main.py
	```
2. Follow the prompts to authenticate and interact with your Google Sheets

.
```

## References
- [Google Sheets API Python Quickstart](https://developers.google.com/sheets/api/quickstart/python)

## License
This project is licensed under the MIT License.
