import json
from supabase_client import supabase

# Read JSON file
with open("dataset.json", "r", encoding="utf-8") as file:
    dataset = json.load(file)

# Upload data
for item in dataset:
    data = {
        "input": item["input"],
        "output": item["output"]
    }

    response = (
        supabase
        .table("hanchat_ai")
        .insert(data)
        .execute()
    )

    print("Uploaded:", item["input"])

print("✅ Dataset upload completed!")