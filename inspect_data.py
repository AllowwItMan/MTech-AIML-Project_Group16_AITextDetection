import json

file_path = "data/open_qa.jsonl"

total_questions = 0
total_human_answers = 0
total_ai_answers = 0

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        data = json.loads(line)

        total_questions += 1
        total_human_answers += len(data["human_answers"])
        total_ai_answers += len(data["chatgpt_answers"])

print("Total questions:", total_questions)
print("Total human answers:", total_human_answers)
print("Total AI answers:", total_ai_answers)