import json
import logging
import csv

with open('Vietnamese_dataset.json', 'r', encoding='utf-8') as file:
    data = json.load(file)['data']

logging.basicConfig(filename='loggingfile.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')

context_count = 0
question_count = 0
correct_answer_count = 0

with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerow(['context', 'question', 'answer', 'is impossible'])  

    for item in data:
        for paragraph in item.get('paragraphs', []):
            if 'context' in paragraph:
                context_count += 1
                context = paragraph['context']

                logging.info(f"Context: {context}")

                for qa in paragraph.get('qas', []):
                    if 'question' in qa:
                        question_count += 1
                        question = qa['question']

                        logging.info(f"Question: {question}")

                        if not qa['is_impossible'] and qa.get('answers'):
                            answer_text = qa['answers'][0].get('text', '')
                            is_impossible = False
                        else:
                            answer_text = ''
                            is_impossible = True

                        writer.writerow([context, question, answer_text, is_impossible])

                        if not is_impossible:
                            correct_answer_count += 1
                    else:
                        logging.warning("Invalid question format")
            else:
                logging.warning("No context found in paragraph")

print("Number of context:", context_count)
print("Number of question:", question_count)
print("Number of correct answers:", correct_answer_count)
