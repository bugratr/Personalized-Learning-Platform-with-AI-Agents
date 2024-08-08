from flask import Flask, render_template, request
from agents import HomeworkCheckerAgent, FeedbackAgent

app = Flask(__name__)

# Create agents
homework_checker_agent = HomeworkCheckerAgent("homework_checker")
feedback_agent = FeedbackAgent("feedback_agent")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_homework', methods=['POST'])
def check_homework():
    homework_text = request.form['homework']
    # Homework checker agent checks the homework
    checked_homework = homework_checker_agent.check_homework(homework_text)
    # Feedback agent provides feedback on the checked homework
    feedback = feedback_agent.provide_feedback(checked_homework)
    return render_template('index.html', checked_homework=checked_homework, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)