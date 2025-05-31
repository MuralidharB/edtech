import json

# Load the previous collection
collection_path = "enrollment_service_test_suite_fixed_grade.postman_collection.json"
with open(collection_path) as f:
    collection = json.load(f)

# Update "Create Grade" request body to match the full GradeCreate schema
for item in collection["item"]:
    if item["name"] == "Create Grade":
        item["request"]["body"]["raw"] = json.dumps({
            "name": "Grade 1",
            "level": 1,
            "curriculum": "CBSE"
        })

# Save updated collection
output_path = "enrollment_service_test_suite_final_grade.postman_collection.json"
with open(output_path, "w") as f:
    json.dump(collection, f, indent=2)

output_path

