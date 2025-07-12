
from fastapi import FastAPI, Request
import httpx
import os

app = FastAPI()

AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")

@app.post("/squarespace-order")
async def receive_order(request: Request):
    data = await request.json()

    # Extract booking names from customFormFields
    fields = data.get("customFormFields", [])
    booking = next((f for f in fields if f["label"] == "Booking Names"), None)

    if not booking:
        return {"error": "Booking Names not found"}

    names = booking["value"].split("\n")
    formatted_names = ", ".join(names)

    airtable_payload = {
        "fields": {
            "Names": formatted_names,
            "Order ID": data.get("orderNumber", "Unknown")
        }
    }

    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }

    airtable_url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"

    async with httpx.AsyncClient() as client:
        response = await client.post(airtable_url, headers=headers, json=airtable_payload)

    return {"status": "success", "airtable_response": response.status_code}
