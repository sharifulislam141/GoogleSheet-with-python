import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
# Step 1: Define API scopes
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

# Step 2: Authorize with JSON
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Step 3: Open Google Sheet by ID
SHEET_ID = "11B23E8ek32OyefEnYwP6ldehzdd0vx1PjxM771N3QOU"
sheet = client.open_by_key(SHEET_ID).sheet1   # first sheet

# Step 4: Read all rows
rows = sheet.get_all_values()

# # Print rows
# print("🔹 Google Sheet Data:")
# for row in rows:
#     print(row)
#add row
#DK Company A/S	La Cours Vej 6	7430	Ikast	96600700	info@dkcompany.com	24431118	www.dkcompany.com	Økonomi	Direktør	Jens Obel Jørgensen	jens@kaffe-clothing.com	https://dk.linkedin.com/in/jens-obel-9514538
sheet.append_row(["DK Company A/S", "La Cours Vej 6", "7430", "Ikast", "96600700", "info@dkcompany.com", "24431118", "www.dkcompany.com", "Økonomi", "Direktør", "Jens Obel Jørgensen", "jens@kaffe-clothing.com", "https://dk.linkedin.com/in/jens-obel-9514538"]) 
sheet.update_acell('A13','Prime Clothing A/S')
data = sheet.get_all_records()
df =pd.DataFrame(data)
print(df)