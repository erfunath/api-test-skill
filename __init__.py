from mycroft import MycroftSkill, intent_file_handler


class ApiTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.api.intent')
    def handle_test_api(self, message):
        self.speak_dialog('test.api')


def create_skill():
    return ApiTest()

