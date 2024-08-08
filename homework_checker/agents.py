from autogen import AssistantAgent, UserProxyAgent

class HomeworkCheckerAgent(AssistantAgent):
    def __init__(self, name):
        super().__init__(name)
    
    def check_homework(self, homework_text):
        message = f"Please check the following homework for any errors: {homework_text}"
        self.initiate_chat(message=message)
        return self.get_response()

class FeedbackAgent(AssistantAgent):
    def __init__(self, name):
        super().__init__(name)
    
    def provide_feedback(self, checked_homework):
        message = f"Provide feedback for the following checked homework: {checked_homework}"
        self.initiate_chat(message=message)
        return self.get_response()