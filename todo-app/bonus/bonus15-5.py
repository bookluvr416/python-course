import json

def get_questions():
    with open("files/questions.json", 'r') as file:
        content = file.read()
    return json.loads(content)

def get_answers(questions_list):
    for question in questions_list:
        text = question["question"]

        for index, answer in enumerate(question["answers"]):
            text = text + f"\n{index + 1}. {answer}"

        try:
            print(text)
            user_answer = int(input("Enter your answer: "))
        except ValueError:
            exit("Invalid number entered.")

        question["user_choice"] = user_answer

def check_answers(questions_list):
    correct_count = 0
    for index, question in enumerate(questions_list):
        if question["correct_answer_key"] == question["user_choice"]:
            correct_count = correct_count + 1
            print(f"{index + 1}. Correct answer. Answer: {question['correct_answer_key']}")
        else:
            print(f"{index + 1}. Incorrect answer. User Answer: {question["user_choice"]}, Correct Answer: {question['correct_answer_key']}")
    print(f"Score: {correct_count} / {len(questions_list)}")

questions = get_questions()
get_answers(questions)
check_answers(questions)



