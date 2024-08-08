from flask import Flask, render_template, request
from agents import QuestionGeneratorAgent, ExamEvaluatorAgent, FeedbackAgent

app = Flask(__name__)

# Create agents
question_generator_agent = QuestionGeneratorAgent("question_generator")
exam_evaluator_agent = ExamEvaluatorAgent("exam_evaluator")
feedback_agent = FeedbackAgent("feedback_agent")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_questions', methods=['POST'])
def generate_questions():
    subject = request.form['subject']
    difficulty = request.form['difficulty']
    # Question generator agent generates questions
    questions = question_generator_agent.generate_questions(subject, difficulty)
    return render_template('index.html', questions=questions)

@app.route('/evaluate_exam', methods=['POST'])
def evaluate_exam():
    answers = request.form['answers']
    correct_answers = request.form['correct_answers']
    # Exam evaluator agent evaluates the answers
    evaluation = exam_evaluator_agent.evaluate_exam(answers, correct_answers)
    # Feedback agent provides feedback on the evaluation
    feedback = feedback_agent.provide_feedback(evaluation)
    return render_template('index.html', evaluation=evaluation, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)