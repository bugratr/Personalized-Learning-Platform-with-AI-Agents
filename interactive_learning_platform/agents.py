from autogen import AssistantAgent

class EducationMaterialAgent(AssistantAgent):
    def __init__(self, name):
        super().__init__(name)
    
    def provide_material(self, topic):
        message = f"Provide detailed educational material on the topic: {topic}."
        self.initiate_chat(message=message)
        return self.get_response()

class QuestionAnsweringAgent(AssistantAgent):
    def __init__(self, name):
        super().__init__(name)
    
    def answer_question(self, question):
        message = f"Answer the following question: {question}."
        self.initiate_chat(message=message)
        return self.get_response()

class ProgressTrackingAgent(AssistantAgent):
    def __init__(self, name):
        super().__init__(name)
    
    def track_progress(self, student_name, activities):
        message = f"Track the progress of {student_name} based on the following activities: {activities}."
        self.initiate_chat(message=message)
        return self.get_response()