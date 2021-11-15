from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class TestSkill(MycroftSkill):

    def __init__(self):
        super().__init__()
        self.learning = True

    def initialize(self):
        my_setting = self.settings.get('my_setting')

    @intent_handler(IntentBuilder('TestIntent').require('TestKeyword'))
    def handle_not_are_you_intent(self, message):
        self.speak_dialog("Test")     

    def stop(self):
        pass

def create_skill():
    return TestSkill()
