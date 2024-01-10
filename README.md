# Quiz Game

## Overview
This Python code represents a simple quiz game. It utilizes a set of questions and answers from an external data source to create a quiz. The user interacts with the quiz through the `QuizBrain` class, answering questions and receiving a final score at the end.

## Components

1. **question_data**: External data containing questions and correct answers.
2. **question_model**: Defines the `Question` class for creating question objects.
3. **quiz_brain**: Implements the `QuizBrain` class responsible for managing the quiz, presenting questions, and tracking the user's score.

## Usage

1. **Create Data and Classes**: The code begins by importing the necessary data and classes.

    ```python
    from data import question_data
    from question_model import Question
    from quiz_brain import QuizBrain
    ```

2. **Build Question Bank**: The script then iterates through the provided `question_data` to create a list of `Question` objects. These objects are stored in the `question_bank`.

    ```python
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    ```

3. **Initialize Quiz**: The `QuizBrain` class is instantiated with the question bank.

    ```python
    quiz = QuizBrain(question_bank)
    ```

4. **Run Quiz Loop**: The quiz loop runs until there are no more questions. The user is prompted with each question, and the user's input is processed by the `QuizBrain` class.

    ```python
    while quiz.still_has_question:
        quiz.next_question()
    ```

5. **Display Final Score**: After completing the quiz, the script prints the user's final score.

    ```python
    print("You have completed the quiz.")
    print(f"Your final score was {quiz.score}/{quiz.question_number}")
    ```

## Instructions for Running

1. Ensure that the required data files (`data.py`, `question_model.py`, `quiz_brain.py`) are present in the same directory as the main script.
2. Run the script using a Python interpreter.

```bash
python quiz_game.py
