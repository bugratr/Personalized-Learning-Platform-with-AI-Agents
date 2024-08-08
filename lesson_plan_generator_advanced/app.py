from flask import Flask, render_template, request
from agents import TeacherAgent, ContentCreatorAgent, CriticAgent

app = Flask(__name__)

# Create agents
teacher_agent = TeacherAgent("teacher")
content_creator_agent = ContentCreatorAgent("content_creator")
critic_agent = CriticAgent("critic")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    subject = request.form['subject']
    # Teacher agent requests a lesson plan
    teacher_agent.request_lesson_plan(subject)
    # Content creator agent creates the lesson content
    content_response = content_creator_agent.create_content(subject)
    # Critic agent reviews the created content
    review_response = critic_agent.review_content(content_response)
    return render_template('index.html', plan=review_response)

if __name__ == '__main__':
    app.run(debug=True)