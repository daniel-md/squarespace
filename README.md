
# Squarespace to Airtable FastAPI

## Setup

1. Create a Python 3.9+ environment
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Set environment variables:
- AIRTABLE_API_KEY
- AIRTABLE_BASE_ID
- AIRTABLE_TABLE_NAME

4. Run the app:
```
uvicorn main:app --host 0.0.0.0 --port 10000
```

5. Use the URL `/squarespace-order` as your Squarespace webhook URL.

## What it does

- Receives Squarespace order JSON POSTs
- Extracts "Booking Names" from custom form fields
- Sends formatted names and order ID to Airtable table
