import random
score = 0
imp = ''
questions = [
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["5", "6", "8", "9"],
        "fail_message": "nice",
        "pass_message": "epic sigma",
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["func", "define", "def", "function"],
        "fail_message": "nice",
        "pass_message": "epic sigma",
    },
    {
        "question": "What is the output of len('hello')?",
        "options": ["4", "5", "6", "Error"],
        "fail_message": "nice",
        "pass_message": "epic sigma",
    }
]

while (True):
    print(questions[score]["question"])
    print('A:'+ questions[score]["options"][0])
    print('B:'+ questions[score]["options"][1])
    print('C:'+ questions[score]["options"][2])
    print('D:'+ questions[score]["options"][3])
    imp = input()