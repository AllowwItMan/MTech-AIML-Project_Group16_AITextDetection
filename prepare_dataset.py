import json
import csv

# Location of the original HC3 dataset
input_file = "data/open_qa.jsonl"

# Location where our cleaned dataset will be saved
output_file = "data/sample_data.csv"

# For now, we are using only 500 questions
num_questions = 500

rows = []

# Read the JSONL file one line at a time
with open(input_file, "r", encoding="utf-8") as file:

    for i, line in enumerate(file):

        # Stop after collecting the first 100 questions
        if i >= num_questions:
            break

        data = json.loads(line)

        question = data["question"]

        # We use the first human answer and first AI answer
        # from each question to keep the dataset consistent
        human_text = data["human_answers"][0]
        ai_text = data["chatgpt_answers"][0]

        # Add the human-written passage
        rows.append([
            f"{i + 1}_human",
            question,
            "human",
            0,
            human_text
        ])

        # Add the original AI-generated passage
        rows.append([
            f"{i + 1}_ai_original",
            question,
            "ai_original",
            1,
            ai_text
        ])

# Create the CSV file containing our selected passages
with open(output_file, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    # Define the column names
    writer.writerow([
        "id",
        "question",
        "text_type",
        "label",
        "text"
    ])

    # Write all collected passages into the CSV
    writer.writerows(rows)

print("Dataset created successfully.")
print("Number of questions:", num_questions)
print("Number of passages:", len(rows))
print("Saved to:", output_file)