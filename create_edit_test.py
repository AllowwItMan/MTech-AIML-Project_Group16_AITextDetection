import csv

input_file = "data/sample_data.csv"
output_file = "data/edited_test.csv"

rows = []

# Read the existing dataset
with open(input_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Select only original AI passages
        if row["text_type"] == "ai_original":
            rows.append(row)

        # We only need 5 passages for our initial test
        if len(rows) == 5:
            break

# Save the 5 passages for editing
with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["id", "question", "text_type", "label", "text"]
    )

    writer.writeheader()
    writer.writerows(rows)

print("Test file created successfully.")
print("Number of AI passages:", len(rows))
print("Saved to:", output_file)