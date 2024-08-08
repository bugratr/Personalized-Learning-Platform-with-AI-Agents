from flask import Flask, render_template, request
from agents import GradeRecorderAgent, ProgressAnalyzerAgent, FeedbackAgent

app = Flask(__name__)

# Create agents
grade_recorder_agent = GradeRecorderAgent("grade_recorder")
progress_analyzer_agent = ProgressAnalyzerAgent("progress_analyzer")
feedback_agent = FeedbackAgent("feedback_agent")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/record_grades', methods=['POST'])
def record_grades():
    student_name = request.form['student_name']
    grades = request.form['grades']
    # Grade recorder agent records the grades
    record_response = grade_recorder_agent.record_grades(student_name, grades)
    return render_template('index.html', record_response=record_response)

@app.route('/analyze_progress', methods=['POST'])
def analyze_progress():
    student_name = request.form['student_name']
    grades = request.form['grades']
    # Progress analyzer agent analyzes the grades
    analysis = progress_analyzer_agent.analyze_progress(student_name, grades)
    # Feedback agent provides feedback on the analysis
    feedback = feedback_agent.provide_feedback(analysis)
    return render_template('index.html', analysis=analysis, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)