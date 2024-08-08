from autogen import AssistantAgent, UserProxyAgent

class GradeRecorderAgent(AssistantAgent):
    def __init__(self, name):
        super().__init__(name)
    
    def record_grades(self, student_name, grades):
        message = f"Record the following grades for {student_name}: {grades}."
        self.initiate_chat(message=message)
        return self.get_response()

class ProgressAnalyzerAgent(AssistantAgent):
    def __init__(self, name):
        super().__init__(name)
    
    def analyze_progress(self, student_name, grades):
        message = f"Analyze the progress of {student_name} with these grades: {grades}."
        self.initiate_chat(message=message)
        return self.get_response()

class FeedbackAgent(AssistantAgent):
    def __init__(self, name):
        super().__init__(name)
    
    def provide_feedback(self, analysis):
        message = f"Provide feedback for the following analysis: {analysis}"
        self.initiate_chat(message=message)
        return self.get_response()