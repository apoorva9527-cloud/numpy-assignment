import json

# 1. Store JSON-formatted string
api_response = '''
{
    "id": "req_123",
    "status": "success",
    "result": {
        "text": "Hello world",
        "confidence": 0.98
    }
}
'''

# 2. Parse JSON string into Python object
data = json.loads(api_response)

# 3. Extract values
request_id = data["id"]
status = data["status"]
text_result = data["result"]["text"]
confidence_score = data["result"]["confidence"]

# Print extracted values
print("Request ID:", request_id)
print("Status:", status)
print("Text:", text_result)
print("Confidence:", confidence_score)

# 4. Warning if confidence < 0.9
if confidence_score < 0.9:
    print("Warning: Confidence score is below acceptable threshold!")

# 5. Create follow-up result dictionary
follow_up = {
    "request_id": request_id,
    "processed": True,
    "message": "Result processed successfully"
}

# Convert dictionary to JSON
json_output = json.dumps(follow_up, indent=4)

# 6. Write JSON output to file
with open("response.json", "w") as file:
    file.write(json_output)

print("JSON response saved to response.json")