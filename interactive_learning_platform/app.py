from flask import Flask, render_template, request
from agents import EducationMaterialAgent, QuestionAnsweringAgent, ProgressTrackingAgent

app = Flask(__name__)

# Create agents
education_material_agent = EducationMaterialAgent("education_material")
question_answering_agent = QuestionAnsweringAgent("question_answering")
progress_tracking_agent = ProgressTrackingAgent("progress_tracking")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_material', methods=['POST'])
def get_material():
    topic = request.form['topic']
    # Education material agent provides material on the topic
    material = education_material_agent.provide_material(topic)
    return render_template('index.html', material=material)

@app.route('/ask_question', methods=['POST'])
def ask_question():
    question = request.form['question']
    # Question answering agent answers the question
    answer = question_answering_agent.answer_question(question)
    return render_template('index.html', answer=answer)

@app.route('/track_progress', methods=['POST'])
def track_progress():
    student_name = request.form['student_name']
    activities = request.form['activities']
    # Progress tracking agent tracks the student's progress
    progress = progress_tracking_agent.track_progress(student_name, activities)
    return render_template('index.html', progress=progress)

if __name__ == '__main__':
    app.run(debug=True)