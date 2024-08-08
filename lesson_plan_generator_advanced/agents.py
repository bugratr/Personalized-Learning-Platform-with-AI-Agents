from autogen import AssistantAgent, UserProxyAgent

class TeacherAgent(UserProxyAgent):
    def __init__(self, name):
        super().__init__(name)
    
    def request_lesson_plan(self, subject):
        message = f"Can you create a weekly lesson plan for {subject}?"
        self.initiate_chat(message=message)

class ContentCreatorAgent(AssistantAgent):
    def __init__(self, name):
        super().__init__(name)
    
    def create_content(self, subject):
        message = f"Create detailed lesson content for {subject}."
        self.initiate_chat(message=message)
        return self.get_response()

class CriticAgent(AssistantAgent):
    def __init__(self, name):
        super().__init__(name)
    
    def review_content(self, content):
        message = f"Review the following content for any improvements: {content}"
        self.initiate_chat(message=message)
        return self.get_response()