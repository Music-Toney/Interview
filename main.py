import json
import re
import uuid
import time


# generate unique identifiers
def generate_uuid():
    return str(uuid.uuid4())


# parse and separate each question and its answer
def parse_qa_pairs(entry):
    qa_pairs = []
    # regular expressions (eliminate unanswered questions)
    qa_matches = re.findall(r'Headline:\s*"(.*?)"\s*Now answer this question:\s*(.*?)(Yes|No)', entry, re.DOTALL)
    for headline, question, answer in qa_matches:
        qa_pairs.append({
            "id": generate_uuid(),
            "Question": question.strip(),
            "Answer": answer.strip(),
            "tag": "finance"
        })
    return qa_pairs


if __name__ == '__main__':
    # load data
    with open('Headline/test.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    all_qa_pairs = []
    start_time = time.time()

    for record in data:
        entry = record['input']
        qa_pairs = parse_qa_pairs(entry)
        all_qa_pairs.extend(qa_pairs)

    end_time = time.time()
    processing_time = end_time - start_time

    # save json (output.json)
    output_path = 'output.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_qa_pairs, f, ensure_ascii=False, indent=2)

    # statistics
    total_qa_pairs = len(all_qa_pairs)

    print(f"Total number of question-answer pairs: {total_qa_pairs}")
    print(f"Time taken for processing: {processing_time:.2f} seconds")
