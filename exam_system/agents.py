from autogen import AssistantAgent, UserProxyAgent

class QuestionGeneratorAgent(AssistantAgent):
    def __init__(self, name):
        super().__init__(name)
    
    def generate_questions(self, subject, difficulty):
        message = f"Generate 5 {difficulty} questions for {subject}."
        self.initiate_chat(message=message)
        return self.get_response()

class ExamEvaluatorAgent(AssistantAgent):
    def __init__(self, name):
        super().__init__(name)
    
    def evaluate_exam(self, answers, correct_answers):
        message = f"Evaluate the following answers: {answers} with correct answers: {correct_answers}."
        self.initiate_chat(message=message)
        return self.get_response()

class FeedbackAgent(AssistantAgent):
    def __init__(self, name):
        super().__init__(name)
    
    def provide_feedback(self, evaluation):
        message = f"Provide feedback for the following evaluation: {evaluation}"
        self.initiate_chat(message=message)
        return self.get_response()